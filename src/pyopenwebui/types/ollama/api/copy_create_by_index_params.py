# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CopyCreateByIndexParams"]


class CopyCreateByIndexParams(TypedDict, total=False):
    destination: Required[str]

    source: Required[str]
