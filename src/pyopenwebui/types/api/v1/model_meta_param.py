# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias, TypedDict

__all__ = ["ModelMetaParam"]


class ModelMetaParamTyped(TypedDict, total=False):
    capabilities: Optional[object]

    description: Optional[str]

    profile_image_url: Optional[str]


ModelMetaParam: TypeAlias = Union[ModelMetaParamTyped, Dict[str, object]]
