# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Optional

from ...._models import BaseModel

__all__ = ["ModelMeta"]


class ModelMeta(BaseModel):
    capabilities: Optional[object] = None

    description: Optional[str] = None

    profile_image_url: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
