from infrastructure.mongo_repository import MongoRepository
import pytest

@pytest.fixture
def mongo_repository():
    repository = MongoRepository(
        "mongodb://mongo:mongo@localhost:27017/",
        "test",
        "test"
    )
    yield repository


@pytest.mark.asyncio
async def test_delete_all(mongo_repository):
    result = await mongo_repository.delete_many({})
    assert result.acknowledged is True


@pytest.mark.asyncio
async def test_insert_one(mongo_repository):
    data = {"name": "test"}
    await mongo_repository.delete_many({})
    result = await mongo_repository.insert(data)
    record = await mongo_repository.find({"_id": result.inserted_id})
    assert result.acknowledged
    assert result.inserted_id is not None
    assert record["_id"] == result.inserted_id
    assert record["name"] == data["name"]

@pytest.mark.asyncio
async def test_find(mongo_repository):
    await mongo_repository.delete_many({})
    result = await mongo_repository.insert({"name": "test"})
    created_data = await mongo_repository.find({"_id": result.inserted_id})
