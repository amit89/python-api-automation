import requests
from requests import Response, RequestException
from .logger import CustomLogger

"""
This class consist all the methods required to make http requests like GET, POST, PUT 
"""
logger = CustomLogger("HttpSession")


class RequestTypes:
    GET = requests.get
    POST = requests.post
    PUT = requests.put
    DELETE = requests.delete


class HttpSession:

    @staticmethod
    def send_request(request_type: RequestTypes, endpoint: str, header_val: dict, payload=None, *args, **kwargs):
        try:
            response: Response = request_type(endpoint, data=payload, headers=header_val, verify=False)
            logger.log_debug("Status code returned by the api : ".format(response.status_code))
            logger.log_debug("Response returned by the api : ".format(response.json()))
            return response.json()

        except RequestException as e:
            logger.log_error("While calling the endpoint encountered as error: ".format(request_type, e))

    @staticmethod
    def send_put_request(endpoint: str, header_val: dict, payload=None, *args, **kwargs):
        try:
            response: Response = RequestTypes.PUT(endpoint, data=payload, headers=header_val, verify=False)
            logger.log_debug("Status code returned by the api : "+ str(response.status_code))
            return response.status_code

        except RequestException as e:
            logger.log_error("While calling the endpoint encountered as error: ".format(RequestTypes, e))

    @staticmethod
    def token(endPoint, header, payload):
        response = HttpSession.send_request(RequestTypes.POST, endPoint, header,
                                            payload)
        token: str = response['access_token']
        token_val: str = "".join('Bearer ' + token)
        logger.log_info("Token created: " + token_val)
        return {"Authorization": token_val, "Content-Type": "application/json"}
