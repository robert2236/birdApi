from motor.motor_asyncio import AsyncIOMotorClient
import datetime


client = AsyncIOMotorClient('mongodb://localhost:27017/')

database = client.birdApi
birds = database.birds

