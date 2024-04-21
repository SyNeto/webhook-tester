import motor.motor_asyncio
from bson import ObjectId
from functools import wraps
from dataclasses import dataclass, field


def convert_id_arg(func):
    """Converts _id field in query data to ObjectId."""
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        if 'query' in kwargs and '_id' in kwargs['query'] and isinstance(kwargs['query']['_id'], str):
            kwargs['query']['_id'] = ObjectId(kwargs['query']['_id'])
        return await func(self, *args, **kwargs)
    return wrapper


@dataclass
class MongoRepository:
    """
    Async MongoDB repository.
    """

    connection_string: str
    db_name: str
    collection_name: str
    client: motor.motor_asyncio.AsyncIOMotorClient = field(init=False)
    db: motor.motor_asyncio.AsyncIOMotorDatabase = field(init=False)
    collection: motor.motor_asyncio.AsyncIOMotorCollection = field(init=False)

    def __post_init__(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.connection_string)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

    @convert_id_arg
    async def find(self, query: dict):
        return await self.collection.find_one(query)

    async def find_many(self, query: dict):
        return self.collection.find(query)

    async def insert(self, data: dict):
        return await self.collection.insert_one(data)

    async def insert_many(self, data: list):
        return await self.collection.insert_many(data)

    @convert_id_arg
    async def update(self, query: dict, data: dict):
        return await self.collection.update_one(query, {"$set": data})
     
    async def updata_many(self, query: dict, data: dict):
        """
        Update multiple documents that match the query.
        query id's must be converted to a valid ObjectId
        """
        return await self.collection.update_many(query, {"$set": data})

    @convert_id_arg
    async def delete(self, query: dict):
        return await self.collection.delete_one(query)
    
    async def delete_many(self, query: dict):
        return await self.collection.delete_many(query)
