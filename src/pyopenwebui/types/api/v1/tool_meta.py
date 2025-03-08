# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ToolMeta"]


class ToolMeta(BaseModel):
    description: Optional[str] = None

    manifest: Optional[object] = None
