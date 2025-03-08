# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ......_models import BaseModel

__all__ = ["BatchProcessFilesResult"]


class BatchProcessFilesResult(BaseModel):
    file_id: str

    status: str

    error: Optional[str] = None
