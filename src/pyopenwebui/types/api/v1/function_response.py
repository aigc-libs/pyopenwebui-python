# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel
from .function_meta import FunctionMeta

__all__ = ["FunctionResponse"]


class FunctionResponse(BaseModel):
    id: str

    created_at: int

    is_active: bool

    is_global: bool

    meta: FunctionMeta

    name: str

    type: str

    updated_at: int

    user_id: str
