# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["FolderModel"]


class FolderModel(BaseModel):
    id: str

    created_at: int

    name: str

    updated_at: int

    user_id: str

    is_expanded: Optional[bool] = None

    items: Optional[object] = None

    meta: Optional[object] = None

    parent_id: Optional[str] = None
