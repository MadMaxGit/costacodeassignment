from graphene import Schema
from app.graphql.queries import Query
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_playground_handler

mockoon_url = 'http://localhost:1337/vehicle/info'

schema = Schema(query=Query) #Graphene is a Python library for building GraphQL APIs

app = FastAPI() #Web Framework for building PIS with Python

app.mount("/graphql", GraphQLApp(
   schema=schema,
   on_get=make_playground_handler() #Starlette is a ASGI framework
   ))