# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .tool_meta_param import ToolMetaParam

__all__ = ["ToolCreateParams"]


class ToolCreateParams(TypedDict, total=False):
    id: Required[str]

    content: Required[str]

    meta: Required[ToolMetaParam]

    name: Required[str]

    access_control: Optional[object]
