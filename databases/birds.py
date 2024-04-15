from databases.database import birds
from models.birds import UpdateBird
from bson import ObjectId

async def get_all_birds():
    bird_list = []
    cursor = birds.find({})
    async for document in cursor:
        bird_list.append(birds(**document))
    return bird_list

async def get_one_bird(species):
    bird = await birds.find_one({"species": species})
    return bird


async def create_bird(bird):
    new_bird = await birds.insert_one(bird)
    created_bird = await birds.find_one({"_id": new_bird.inserted_id})
    return created_bird

async def update_bird(id: str, data: UpdateBird):
    bird = {k: v for k, v in data.dict().items() if v is not None}
    await birds.update_one({"_id": ObjectId(id)}, {"$set": bird})
    document = await birds.find_one({"_id": ObjectId(id)})
    return document

async def delete_bird(id):
    await birds.delete_one({"_id": ObjectId(id)})
    return True
