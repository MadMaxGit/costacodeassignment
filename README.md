# costacodeassignment
To implement a simplified version of the GraphQL serving application.

# Setup a Python Virtual Environment

On the terminal
```
python -m venv env
```

# Activate the virtual enivronment

```
.\env\Scripts\activate
```

# Setup
1. Created of Mongo DB in Cloud which is called as Mongo DB Atlas.
2. Start the Mockoon Server and check the Port it is running, mostly in port 1337.
3. Install the Python and python intrepeter.
4. IDE for Coding, like Visual Code.
5. Install python web framework FastAPI, Graphene, Starlette, Uvicorn, pymongo

```
pip install pymongo, uvicorn, graphene, fastapi
```


# Start the Apllication

On the virtual Environment terminal
```
uvicorn app.main:app --reload
```

# API

To Fetch and store the Mock Data from Mockoon server use below GET request

```
GET http://127.0.0.1:8000/fetch_and_store
```

To query the Data use the below playground which is mounted on the Graphene Starlette 

```
GET http://127.0.0.1:8000/graphql/
```

