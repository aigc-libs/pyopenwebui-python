# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .message_user_response import MessageUserResponse

__all__ = ["MessageGetResponse"]

MessageGetResponse: TypeAlias = List[MessageUserResponse]
