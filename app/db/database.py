#from app.settings.config import DB_URL
from pymongo import MongoClient
from os import getenv

db_url = getenv("DB_URL")

# Connect to MongoDB
client = MongoClient(db_url)
db = client["costacodeassignment"]  # Replace "your_database" with your database name
collection = db["vehicles"]  # Replace "your_collection" with your collection name
