# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .function_meta_param import FunctionMetaParam

__all__ = ["FunctionCreateParams"]


class FunctionCreateParams(TypedDict, total=False):
    id: Required[str]

    content: Required[str]

    meta: Required[FunctionMetaParam]

    name: Required[str]
