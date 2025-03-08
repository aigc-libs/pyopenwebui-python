# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .function_meta import FunctionMeta

__all__ = ["FunctionModel"]


class FunctionModel(BaseModel):
    id: str

    content: str

    created_at: int

    meta: FunctionMeta

    name: str

    type: str

    updated_at: int

    user_id: str

    is_active: Optional[bool] = None

    is_global: Optional[bool] = None
