# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PromptCreateParams"]


class PromptCreateParams(TypedDict, total=False):
    command: Required[str]

    content: Required[str]

    title: Required[str]
