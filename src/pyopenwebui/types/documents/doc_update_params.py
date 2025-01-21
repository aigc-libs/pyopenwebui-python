# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DocUpdateParams"]


class DocUpdateParams(TypedDict, total=False):
    name_1: Required[Annotated[str, PropertyInfo(alias="name")]]

    name_2: Required[Annotated[str, PropertyInfo(alias="name")]]

    title: Required[str]
