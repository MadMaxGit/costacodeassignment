from graphene import ObjectType, String, List, Field
from app.graphql.types import VehicleEntity
from loguru import logger
from app.db.database import collection

class Query(ObjectType):
    vehicleById = Field(VehicleEntity, vehicleId=String(required=True))
    vehiclesByPartialName = List(VehicleEntity, partialName=String(required=True))
    vehiclesByServiceStatus = List(
        VehicleEntity,
        serviceName=String(required=True),
        serviceStatus=String(required=True)
    )

    def resolve_vehicleById(self, info, vehicleId):
        vehicle = collection.find_one({"id": vehicleId})
        if vehicle:
            return VehicleEntity(id=vehicle['id'], name=vehicle['name'], services=vehicle['services'])
        else:
            return None

    def resolve_vehiclesByPartialName(self, info, partialName):
        vehicles = collection.find({"name": {"$regex": partialName, "$options": "i"}})
        return [VehicleEntity(id=vehicle['id'], name=vehicle['name'], services=vehicle['services']) for vehicle in vehicles]

    def resolve_vehiclesByServiceStatus(self, info, serviceName, serviceStatus):
        vehicles = collection.find({"services": {"$elemMatch": {"serviceName": serviceName, "status": serviceStatus}}})
        return [VehicleEntity(id=vehicle['id'], name=vehicle['name'], services=vehicle['services']) for vehicle in vehicles]