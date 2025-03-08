# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1.chats.pinned_get_response import PinnedGetResponse
from .....types.api.v1.chats.pinned_list_response import PinnedListResponse

__all__ = ["PinnedResource", "AsyncPinnedResource"]


class PinnedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PinnedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return PinnedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PinnedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/pyopenwebui-python#with_streaming_response
        """
        return PinnedResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PinnedListResponse:
        """Get User Pinned Chats"""
        return self._get(
            "/api/v1/chats/pinned",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PinnedListResponse,
        )

    def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PinnedGetResponse]:
        """
        Get Pinned Status By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v1/chats/{id}/pinned",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PinnedGetResponse,
        )


class AsyncPinnedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPinnedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPinnedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPinnedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/pyopenwebui-python#with_streaming_response
        """
        return AsyncPinnedResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PinnedListResponse:
        """Get User Pinned Chats"""
        return await self._get(
            "/api/v1/chats/pinned",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PinnedListResponse,
        )

    async def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PinnedGetResponse]:
        """
        Get Pinned Status By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v1/chats/{id}/pinned",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PinnedGetResponse,
        )


class PinnedResourceWithRawResponse:
    def __init__(self, pinned: PinnedResource) -> None:
        self._pinned = pinned

        self.list = to_raw_response_wrapper(
            pinned.list,
        )
        self.get = to_raw_response_wrapper(
            pinned.get,
        )


class AsyncPinnedResourceWithRawResponse:
    def __init__(self, pinned: AsyncPinnedResource) -> None:
        self._pinned = pinned

        self.list = async_to_raw_response_wrapper(
            pinned.list,
        )
        self.get = async_to_raw_response_wrapper(
            pinned.get,
        )


class PinnedResourceWithStreamingResponse:
    def __init__(self, pinned: PinnedResource) -> None:
        self._pinned = pinned

        self.list = to_streamed_response_wrapper(
            pinned.list,
        )
        self.get = to_streamed_response_wrapper(
            pinned.get,
        )


class AsyncPinnedResourceWithStreamingResponse:
    def __init__(self, pinned: AsyncPinnedResource) -> None:
        self._pinned = pinned

        self.list = async_to_streamed_response_wrapper(
            pinned.list,
        )
        self.get = async_to_streamed_response_wrapper(
            pinned.get,
        )
