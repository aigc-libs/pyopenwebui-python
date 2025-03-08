# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .tool_meta import ToolMeta
from ...._models import BaseModel
from .user_response import UserResponse

__all__ = ["ToolUserResponse"]


class ToolUserResponse(BaseModel):
    id: str

    created_at: int

    meta: ToolMeta

    name: str

    updated_at: int

    user_id: str

    access_control: Optional[object] = None

    user: Optional[UserResponse] = None
