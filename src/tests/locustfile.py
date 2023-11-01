import json

from locust import task, SequentialTaskSet, HttpUser, between
import locust.stats
from src.core.request import HttpSession
from src.config.payload import get_payload
from src.config.endpoints import EndPoints
from src.config.constants import Constants
from src.core.logger import CustomLogger

logger = CustomLogger("Performance Test")

locust.stats.CSV_STATS_INTERVAL_SEC = 5
locust.stats.CSV_STATS_FLUSH_INTERVAL_SEC = 60


class BackOfficeServices(SequentialTaskSet):

    def __init__(self, parent):
        super().__init__(parent)
        self.token = None
        self.payload = None

    def on_start(self):
        self.client.verify = False
        self.token = HttpSession.token(EndPoints.token_url, Constants.token_header(),
                                       Constants.empty_payload())
        self.payload = get_payload()
        logger.log_info(self.payload)

    @task
    def create_users(self):
        response = self.client.post("/api/users", headers=Constants.default_header(), json=json.loads(self.payload))
        logger.log_info(response)

    @task
    def get_users(self):
        self.client.get("/api/users?page=2", headers=Constants.default_header())

    @task
    def get_rehost(self):
        self.client.get("/backoffice/v1/reports/rehost?startTime=2023-06-01T00:00:00Z&endTime=2023-07-01T00:00:00Z&rehostsLimit=3", headers=Constants.rehost_header())


class LoadTesting(HttpUser):
    host = EndPoints.dummy_host
    host = EndPoints.host
    tasks = [BackOfficeServices]
    wait_time = between(2, 5)
