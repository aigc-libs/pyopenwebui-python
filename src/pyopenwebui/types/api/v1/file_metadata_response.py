# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel

__all__ = ["FileMetadataResponse"]


class FileMetadataResponse(BaseModel):
    id: str

    created_at: int

    meta: object

    updated_at: int
