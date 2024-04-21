from bson import ObjectId
from models.webhook import Webhook  # Adjust the import path as necessary

def test_webhook_model_creation():
    # Test successful creation
    webhook1_data = {
        "_id": "123456789012345678901234",
        "token": "some_token",
        "method": "POST",
        "created_at": "2021-01-01T00:00:00",
        "updated_at": "2021-01-01T00:00:00",
        "deleted_at": "2021-01-01T00:00:00",
    }
    webhook2_data = {
        "id": ObjectId("123456789012345678901234"),
        "token": "some_token",
        "method": "POST",
        "created_at": "2021-01-01T00:00:00",
        "updated_at": "2021-01-01T00:00:00",
        "deleted_at": "2021-01-01T00:00:00",
    }
    webhook1 = Webhook(**webhook1_data)
    webhook2 = Webhook(**webhook2_data)
    assert webhook1.token == "some_token"
    assert webhook1.method == "POST"
    assert webhook2.token == "some_token"
    assert webhook2.method == "POST"


def test_webhook_model_default_values():
    # Test default values
    webhook = Webhook(token="some token", method="POST")
    assert webhook.created_at is None
    assert webhook.updated_at is None
    assert webhook.deleted_at is None
    assert webhook.token == "some token"
    assert webhook.method == "POST"
