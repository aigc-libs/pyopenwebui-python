# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo
from ..model_meta_param import ModelMetaParam
from ..model_params_param import ModelParamsParam

__all__ = ["ModelUpdateParams"]


class ModelUpdateParams(TypedDict, total=False):
    id_1: Required[Annotated[str, PropertyInfo(alias="id")]]

    id_2: Required[Annotated[str, PropertyInfo(alias="id")]]

    meta: Required[ModelMetaParam]

    name: Required[str]

    params: Required[ModelParamsParam]

    access_control: Optional[object]

    base_model_id: Optional[str]

    is_active: bool
