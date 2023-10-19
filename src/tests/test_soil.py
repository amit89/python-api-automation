from src.core.request import RequestTypes, HttpSession
from src.config.endpoints import EndPoints
from src.config.payload import soil_test_payload, update_soil_test_payload
from src.core.logger import CustomLogger
from src.core.driver import post_bulk_data

logger = CustomLogger("test")

##chnage the path according to you machine
_file_path: str = "/Users/amitkumar/Documents/BACKEND-PROJ/trimble-agri/test_data/final-sheet.csv"


# def test_create_soil_id(get_token, create_soil_test):
#     soil_id = create_soil_test
#     print(soil_id)
#
#
# def test_update_soil_test(get_token):
#     status_code = HttpSession.send_put_request(EndPoints.update_soil_test, get_token,
#                                                update_soil_test_payload())
#     logger.log_info("Soil test updated with status code: " + str(status_code))
#     assert status_code == 204, f"Expected{204} but getting {status_code}"


def test_post_bulk_data(get_token):
    post_bulk_data(get_token)
