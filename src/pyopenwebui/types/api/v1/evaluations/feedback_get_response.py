# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .feedbacks.feedback_user_response import FeedbackUserResponse

__all__ = ["FeedbackGetResponse"]

FeedbackGetResponse: TypeAlias = List[FeedbackUserResponse]
