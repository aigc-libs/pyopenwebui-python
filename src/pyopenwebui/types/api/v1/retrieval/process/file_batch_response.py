# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ......_models import BaseModel
from .batch_process_files_result import BatchProcessFilesResult

__all__ = ["FileBatchResponse"]


class FileBatchResponse(BaseModel):
    errors: List[BatchProcessFilesResult]

    results: List[BatchProcessFilesResult]
