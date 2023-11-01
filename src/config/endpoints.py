env = "dev"


class EndPoints:
    host = f"https://ansys-licensing-apim-{env}.azure-api.net"
    rehost_endpoint = f"{host}/backoffice/v1/reports/rehost?startTime=2023-06-01T00:00:00Z&endTime=2023-07-01T00:00:00Z&rehostsLimit=3"
    token_url = "https://id.trimble.com/oauth/token?grant_type=client_credentials&scope=Nutrilytical"
    create_soil_test = "https://cloud.api.trimble.com/Trimble-Ag-Software/externalApi/3.0/analytics/e7b47fcb-748c-4650-952f-3f556fa25859/soiltests/"
    update_soil_test = f"https://cloud.api.trimble.com/Trimble-Ag-Software/externalApi/3.0/analytics/e7b47fcb-748c-4650-952f-3f556fa25859/soiltests/bac9bf57-e3d2-40ed-8900-343cf8b57358"
    dummy_host = f"https://reqres.in"
    create_user =f"{dummy_host}/api/users"
    get_users = f"{dummy_host}/api/users?page=2"
