# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel
from .model_meta import ModelMeta
from .model_params import ModelParams
from .user_response import UserResponse

__all__ = ["ModelGetResponse", "ModelGetResponseItem"]


class ModelGetResponseItem(BaseModel):
    id: str

    created_at: int

    is_active: bool

    meta: ModelMeta

    name: str

    params: ModelParams

    updated_at: int

    user_id: str

    access_control: Optional[object] = None

    base_model_id: Optional[str] = None

    user: Optional[UserResponse] = None


ModelGetResponse: TypeAlias = List[ModelGetResponseItem]
