from graphene import ObjectType, String, List, Field


class Query(ObjectType):
 
    def resolve_vehicleById(self, info, vehicleId):
        pass

    def resolve_vehiclesByPartialName(self, info, partialName):
        pass

    def resolve_vehiclesByServiceStatus(self, info, serviceName, serviceStatus):
        pass