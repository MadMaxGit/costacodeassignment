import requests
from app.settings.config import mockoon_URL 
from loguru import logger
logger.add("app1.log", rotation="500 MB") #Remove it after adding

class VehicleMock:
    def __init__(self, vehicle_repository):
        self.vehicle_repository = vehicle_repository

    def fetch_and_store_data(self):
        saved_count = 0
        self.vehicle_repository.drop() #Delete the Data in mongoDB
        try:
            vehicles = self.get_vehicle_list()
            if vehicles:
                for vehicle in vehicles:
                    vehicle_info = self.get_vehicle_info(vehicle)
                    vehicle_service = self.get_vehicle_service(vehicle)
                    vehicle_entity = self.get_validate_entity(vehicle, vehicle_info, vehicle_service)                    
                    try:
                        self.vehicle_repository.insert_one(vehicle_entity)
                        saved_count += 1
                    except Exception as e:
                        logger.info(f"Failed to save entity for Vehicle ID: {vehicle['id']}")
                        # Log the exception or handle it as needed
        except Exception as e:
            # Handle exceptions
            pass
        return saved_count

    def get_validate_entity(self, vehicle, vehicle_info, vehicle_service):
        vehicle_entity = {
            'id': vehicle.get("id"),
            'name': vehicle.get("name") if vehicle_info else None,
            'msidn': vehicle_info.get('msidn') if vehicle_info else None,
            'engineStatus': vehicle_info.get('engineStatus') if vehicle_info else None,
            'fleet': vehicle_info.get('fleet') if vehicle_info else None,
            'brand': vehicle_info.get('brand') if vehicle_info else None,
            'countryOfOperation': vehicle_info.get('countryOfOperation') if vehicle_info else None,
            'chassisNumber': vehicle_info.get('chassisNumber') if vehicle_info else None,
            'cassisSeries': vehicle_info.get('cassisSeries') if vehicle_info else None,
            'communicationStatus': vehicle_service.get('communicationStatus') if vehicle_service else None,
            'services': vehicle_service.get('services') if vehicle_service else None
        }
        return vehicle_entity
    
    def get_vehicle_service(self, vehicle):
        try:
            response = requests.get(f"{mockoon_URL}services?id={vehicle['id']}")
            if response.status_code == 200:
                return response.json()
            else:
                logger.info(f"Non-successful response received for vehicle services: {response.status_code}")
        except Exception as e:
            logger.info(f"Error while fetching vehicle services: {e}")
        return None

    def get_vehicle_info(self, vehicle):
        try:
            response = requests.get(f"{mockoon_URL}info?id={vehicle['id']}")
            if response.status_code == 200:

                return response.json()
            else:
                logger.info(f"Non-successful response received for vehicle info: {response.status_code}")
        except Exception as e:
            logger.info(f"Error while fetching vehicle info: {e}")
        return None

    def get_vehicle_list(self):
        try:
            response = requests.get(f"{mockoon_URL}list")
            if response.status_code == 200:
                data = response.json()
                return data.get('vehicles', [])
            else:
                logger.info(f"Non-successful response received for vehicle list: {response.status_code}")
        except Exception as e:
            logger.info(f"Error while fetching vehicle list: {e}")
        return []