import json

from locust import task, SequentialTaskSet, HttpUser, between
import locust.stats
from src.core.request import HttpSession
from src.config.payload import get_payload
from src.config.endpoints import EndPoints
from src.config.constants import Constants

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
                                       Constants.token_payload())
        self.payload = get_payload()

    @task
    def get_rehost(self):
        #reponse = self.client.post("api/users", json=self.payload, name=f"ENDPOINT NAME")
        response = self.client.post(EndPoints.token_url, headers= Constants.token_header(), json= Constants.token_payload())
        print(response.status_code)


class LoadTesting(HttpUser):
    #host = "https://reqres.in/"
    hots = "https://id.trimble.com"
    tasks = [BackOfficeServices]
    wait_time = between(2, 5)
