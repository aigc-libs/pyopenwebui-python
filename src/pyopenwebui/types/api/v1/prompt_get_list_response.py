# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel
from .user_response import UserResponse

__all__ = ["PromptGetListResponse", "PromptGetListResponseItem"]


class PromptGetListResponseItem(BaseModel):
    command: str

    content: str

    timestamp: int

    title: str

    user_id: str

    access_control: Optional[object] = None

    user: Optional[UserResponse] = None


PromptGetListResponse: TypeAlias = List[PromptGetListResponseItem]
