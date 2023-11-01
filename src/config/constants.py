class Constants:

    @staticmethod
    def token_header() -> dict:
        return {
            'Authorization': 'Basic {{'
                             'NzJmMzlmNWMtNDM5MC00NTllLWIzMDgtODE4OGRhNjgwNTdkOjY4YjFlZWRkZjczOTQxMWM5Y2RlNDRhMDQyOGE3MDEx}}'
        }

    @staticmethod
    def empty_payload() -> dict:
        return {}

    @staticmethod
    def default_header() -> dict:
        return {"content-type": "application/json"}

    @staticmethod
    def rehost_header() -> dict:
        return {
            'Ocp-Apim-Subscription-Key': '673203682d8740e9a4966b7a9b19083a'
        }
