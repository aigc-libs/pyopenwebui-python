# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel
from .user_response import UserResponse
from .file_metadata_response import FileMetadataResponse

__all__ = ["KnowledgeUserResponse", "File"]

File: TypeAlias = Union[FileMetadataResponse, object]


class KnowledgeUserResponse(BaseModel):
    id: str

    created_at: int

    description: str

    name: str

    updated_at: int

    user_id: str

    access_control: Optional[object] = None

    data: Optional[object] = None

    files: Optional[List[File]] = None

    meta: Optional[object] = None

    user: Optional[UserResponse] = None
