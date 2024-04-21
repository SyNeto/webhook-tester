from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from typing_extensions import Annotated


PyObjectId = Annotated[str, str]


class Webhook(BaseModel):

    model_config: ConfigDict = {
        "pupulate_by_name": True,
        "validate_assignment": True
    }

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    token: str
    method: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
