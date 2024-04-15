from fastapi import APIRouter, HTTPException
from databases.birds import (get_all_birds,create_bird,get_one_bird,delete_bird)
from models.birds import Parrot,UpdateBird

bird = APIRouter()

@bird.get('/api/birds')
async def get_birds():
    response = await get_all_birds()
    return response

@bird.post('/api/create_birds', response_model=Parrot)
async def save_bird(bird: Parrot):
    birdFound = await get_one_bird(bird.species)
    if birdFound:
        raise HTTPException(409, "Bird already exists")

    response = await create_bird(bird.dict())
    print(response)
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@bird.put('/api/birds/{id}', response_model=Parrot)
async def put_bird(id: str, data: UpdateBird):
    data.id = id
    response = UpdateBird(**data.dict())
    if response:
        return response
    raise HTTPException(404, f"There is no task with the id {id}")


@bird.delete('/api/birds/{id}')
async def remove_task(id: str):
    response = await delete_bird(id)
    if response:
        return "Successfully bird delete from the database"
    raise HTTPException(404, f"There is no task with the id {id}")
    