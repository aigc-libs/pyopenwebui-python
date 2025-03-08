# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .model_meta_param import ModelMetaParam
from .model_params_param import ModelParamsParam

__all__ = ["ModelCreateParams"]


class ModelCreateParams(TypedDict, total=False):
    id: Required[str]

    meta: Required[ModelMetaParam]

    name: Required[str]

    params: Required[ModelParamsParam]

    access_control: Optional[object]

    base_model_id: Optional[str]

    is_active: bool
