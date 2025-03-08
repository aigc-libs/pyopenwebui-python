# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1.chats import list_user_params
from .....types.api.v1.chats.list_user_response import ListUserResponse

__all__ = ["ListResource", "AsyncListResource"]


class ListResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ListResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return ListResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ListResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return ListResourceWithStreamingResponse(self)

    def user(
        self,
        user_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        skip: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListUserResponse:
        """
        Get User Chat List By User Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/api/v1/chats/list/user/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    list_user_params.ListUserParams,
                ),
            ),
            cast_to=ListUserResponse,
        )


class AsyncListResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncListResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncListResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncListResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncListResourceWithStreamingResponse(self)

    async def user(
        self,
        user_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        skip: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListUserResponse:
        """
        Get User Chat List By User Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/api/v1/chats/list/user/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    list_user_params.ListUserParams,
                ),
            ),
            cast_to=ListUserResponse,
        )


class ListResourceWithRawResponse:
    def __init__(self, list: ListResource) -> None:
        self._list = list

        self.user = to_raw_response_wrapper(
            list.user,
        )


class AsyncListResourceWithRawResponse:
    def __init__(self, list: AsyncListResource) -> None:
        self._list = list

        self.user = async_to_raw_response_wrapper(
            list.user,
        )


class ListResourceWithStreamingResponse:
    def __init__(self, list: ListResource) -> None:
        self._list = list

        self.user = to_streamed_response_wrapper(
            list.user,
        )


class AsyncListResourceWithStreamingResponse:
    def __init__(self, list: AsyncListResource) -> None:
        self._list = list

        self.user = async_to_streamed_response_wrapper(
            list.user,
        )
