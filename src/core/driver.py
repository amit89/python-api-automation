import csv
import json

from src.core.logger import CustomLogger
from src.core.request import HttpSession, RequestTypes
from src.config.endpoints import EndPoints

logger = CustomLogger(__name__)

#### change the path according to you machine
_file_path: str = "/Users/amitkumar/Documents/BACKEND-PROJ/trimble-agri/test_data/final-sheet-copy.csv"
soil_test_id = None
my_var = None


def post_bulk_data(token: dict):
    global my_var
    global soil_test_id

    with open(_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row = convert_fields_to_int(row)
            crop_zone_id = row.get('cropZoneId')
            if my_var != crop_zone_id:
                my_var = crop_zone_id
                payload = json.dumps(row, indent=4)
                logger.log_info("Creating Soil Test ID for crop-zone-id:->" + my_var)
                response = HttpSession.send_request(RequestTypes.POST, EndPoints.create_soil_test, token,
                                                    payload)
                soil_test_id = response["id"]
                logger.log_info("New crop test id has created:->" + soil_test_id)
            else:
                logger.log_info("Updating Soil Test ID for crop-zone-id:->" + my_var)
                update_endpoint = f"https://cloud.api.trimble.com/Trimble-Ag-Software/externalApi/3.0/analytics" \
                                  f"/e7b47fcb-748c-4650-952f-3f556fa25859/soiltests/{soil_test_id}"
                payload = json.dumps(row, indent=4)
                status_code = HttpSession.send_put_request(update_endpoint, token,
                                                           payload)
                logger.log_info("Status of update request is:--" + str(status_code))
                assert status_code == 204, f"Expected{204} but getting {status_code}"


# Function to convert specific fields to integers
def convert_fields_to_int(row):
    int_fields = ['cropYear', 'depthStart', 'depthEnd', 'organicMatter', 'phosphorusP1', 'phosphorusP2', 'phosphorusP',
                  'phosphorusMehlichp', 'saturationP', 'biCarb', 'p1ToP2Ratio', 'potassium', 'magnesium',
                  'kMgRatio', 'calcium', 'phSoil', 'phBuffer', 'sodium', 'cec', 'percentagePotassium',
                  'percentageMagnesium', 'percentageCalcium', 'percentageHydrogen', 'percentageSodium', 'sulphur',
                  'zinc', 'manganese',
                  'iron', 'copper', 'boron', 'nitrates', 'solubleSalts', 'chloride', 'aluminum', 'nToSRatio',
                  'molybdenum', 'nH4', 'urea', 'bulkDensity', 'baseSaturation', 'freeLime', 'moisture']
    for field in int_fields:
        value = row.get(field, None)
        if value:
            # Remove quotes and any leading/trailing spaces
            value = value.strip('"').strip()

            # Check if the value can be converted to an integer or float
            try:
                if '.' in value:
                    row[field] = float(value)
                else:
                    row[field] = int(value)
            except ValueError:
                row[field] = 0
        else:
            row[field] = 0
    return row

