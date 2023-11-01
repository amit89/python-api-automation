import pytest
from src.core.request import HttpSession, RequestTypes
from src.config.endpoints import EndPoints
from src.config.constants import Constants
from src.config.payload import soil_test_payload
from src.core.logger import CustomLogger

"""
This class consist all the data methods required to write test cases
"""
logger = CustomLogger("conftest")


@pytest.fixture(scope="module")
def get_token():
    response = HttpSession.send_request(RequestTypes.POST, EndPoints.token_url, Constants.token_header(),
                                        Constants.empty_payload())[0]
    token: str = response['access_token']
    token_val: str = "".join('Bearer ' + token)
    logger.log_info("Token created: " + token_val)
    return {"Authorization": token_val, "Content-Type": "application/json"}


@pytest.fixture(scope="module")
def create_soil_test(get_token):
    response, status_code = HttpSession.send_request(RequestTypes.POST, EndPoints.create_soil_test, get_token,
                                                     soil_test_payload())
    logger.log_info("New Soil test created with id : " + response['id'])
    return response
