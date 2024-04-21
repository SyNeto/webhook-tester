from abc import ABC, abstractmethod
from dataclasses import dataclass

from models.webhook import Webhook


class WebhookRepositoryInterface(ABC):
    """Interface for webhook repository"""

    @abstractmethod
    async def find(self, query: dict):
        pass

    @abstractmethod
    async def find_many(self, query: dict):
        pass

    @abstractmethod
    async def insert(self, data: dict):
        pass

    @abstractmethod
    async def insert_many(self, data: list):
        pass

    @abstractmethod
    async def update(self, query: dict, data: dict):
        pass

    @abstractmethod
    async def update_many(self, query: dict, data: dict):
        pass

    @abstractmethod
    async def delete(self, query: dict):
        pass

    @abstractmethod
    async def delete_many(self, query: dict):
        pass


@dataclass
class WebhookApp:

    webhook_repository: WebhookRepositoryInterface

    async def create(self, data: dict):
        webhook = Webhook(**data)
        return await self.webhook_repository.insert(
            webhook.model_dump(exclude_none=True)
        )

    async def get(self, query: dict):
        return await self.webhook_repository.find(query)
