from pymongo import MongoClient

DB_URL="mongodb+srv://root:root@cluster0.8vufshx.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
client = MongoClient(DB_URL)
db = client["costacodeassignment"]  # Replace "your_database" with your database name
collection = db["vehicles"]  # Replace "your_collection" with your collection name
