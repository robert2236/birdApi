from typing import Optional
from pydantic import BaseModel, Field, validator
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, values, **kwargs):
     if not ObjectId.is_valid(v):
        raise ValueError('Invalid ObjectId')
     return str(v)
    

class Parrot(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    species: str
    scientific_name: str
    common_name: str
    image_url: str
    endangered: bool
    description: str
    habitat: str
    distribution: str
    diet: str
    behavior: str
    size: str
    lifespan: str
    conservation_status: str

class UpdateBird(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    species: Optional[str] = None
    scientific_name: Optional[str] = None
    common_name: Optional[str] = None
    image_url: Optional[str] = None
    endangered: Optional[bool] = None
    description: Optional[str] = None
    habitat: Optional[str] = None
    distribution: Optional[str] = None
    diet: Optional[str] = None
    behavior: Optional[str] = None
    size: Optional[str] = None
    lifespan: Optional[str] = None
    conservation_status: Optional[str] = None
    user_profile_photo: Optional[str] = None


class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str
        }
