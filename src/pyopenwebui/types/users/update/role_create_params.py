# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RoleCreateParams"]


class RoleCreateParams(TypedDict, total=False):
    id: Required[str]

    role: Required[str]
