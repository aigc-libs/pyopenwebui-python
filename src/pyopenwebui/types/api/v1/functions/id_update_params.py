# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo
from ..function_meta_param import FunctionMetaParam

__all__ = ["IDUpdateParams"]


class IDUpdateParams(TypedDict, total=False):
    id_2: Required[Annotated[str, PropertyInfo(alias="id")]]

    content: Required[str]

    meta: Required[FunctionMetaParam]

    name: Required[str]
