from app.settings.config import DB_URL
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient(DB_URL)
db = client["costacodeassignment"]  # Replace "your_database" with your database name
collection = db["vehicles"]  # Replace "your_collection" with your collection name
