from app.webhook_app import WebhookApp
import pytest
from infrastructure.mongo_repository import MongoRepository


@pytest.fixture
def webhook_app():
    app = WebhookApp(webhook_repository=MongoRepository(
        "mongodb://mongo:mongo@localhost:27017/",
        "webhook",
        "webhooks"
    ))
    yield app


@pytest.mark.asyncio
async def test_create(webhook_app):
    await webhook_app.webhook_repository.delete_many({})
    data = {
        "token": "test_token",
        "method": "POST"
    }
    result = await webhook_app.create(data)
    webhook = await webhook_app.webhook_repository.find({"_id": result.inserted_id})
    assert webhook["_id"] == result.inserted_id
    assert webhook["token"] == data["token"]
    assert webhook["method"] == data["method"]