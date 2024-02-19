from graphene import ObjectType, String, List

class ServiceInfo(ObjectType):
    serviceName = String()
    status = String()
    lastUpdate = String()

class VehicleEntity(ObjectType):
    id = String(required=True)
    name = String()
    msidn = String()
    engineStatus = String()
    fleet = String()
    brand = String()
    countryOfOperation = String()
    chassisNumber = String()
    cassisSeries = String()
    services = List(ServiceInfo)
