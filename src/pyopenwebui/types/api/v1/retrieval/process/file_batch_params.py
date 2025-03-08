# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ...file_model_param import FileModelParam

__all__ = ["FileBatchParams"]


class FileBatchParams(TypedDict, total=False):
    collection_name: Required[str]

    files: Required[Iterable[FileModelParam]]
