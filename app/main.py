from graphene import Schema, ObjectType, String, Int, Field, List
from pymongo import MongoClient

DB_URL="mongodb+srv://root:root@cluster0.8vufshx.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
client = MongoClient('mongodb+srv://root:root@cluster0.8vufshx.mongodb.net/?retryWrites=true&w=majority')
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["costacodeassignment"]  # Replace "your_database" with your database name
collection = db["vehicles"]  # Replace "your_collection" with your collection name

mockoon_url = 'http://localhost:1337/vehicle/info'

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

class UserType(ObjectType):
    id = Int()
    name= String()
    age=Int()
    place= String()


class Query(ObjectType):
 
    def resolve_vehicleById(self, info, vehicleId):
        pass

    def resolve_vehiclesByPartialName(self, info, partialName):
        pass

    def resolve_vehiclesByServiceStatus(self, info, serviceName, serviceStatus):
        pass

gpl_query='''
query{
    user(userId: 1){
        id
        name
        age
        place
    }
}
'''

schema = Schema(query=Query)

if __name__ == "__main__":
    result = schema.execute(gpl_query)