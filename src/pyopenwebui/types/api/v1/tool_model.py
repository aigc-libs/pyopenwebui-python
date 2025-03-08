# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .tool_meta import ToolMeta
from ...._models import BaseModel

__all__ = ["ToolModel"]


class ToolModel(BaseModel):
    id: str

    content: str

    created_at: int

    meta: ToolMeta

    name: str

    specs: List[object]

    updated_at: int

    user_id: str

    access_control: Optional[object] = None
