from graphene import Schema
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_playground_handler
from app.graphql.queries import Query

from loguru import logger
from app.vehiclemock import VehicleMock
from app.db.database import collection

#Adding a Logger Library for logging
logger.add("app.log", rotation="500 MB")

schema = Schema(query=Query) #Graphene is a Python library for building GraphQL APIs

app = FastAPI() #Web Framework for building PIS with Python

vehicle_service = VehicleMock(collection) #Move this to line 21 and check it

@app.get('/fetch_and_store')
async def fetch_store():
    saved_count = vehicle_service.fetch_and_store_data()
    logger.info("Saved {saved_count} records.") #Fix this logik in the later part
    return {'message': f'{saved_count} records stored successfully in MongoDB'}

app.mount("/graphql", GraphQLApp(
   schema=schema,
   on_get=make_playground_handler() #Starlette is a ASGI framework
   ))