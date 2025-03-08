# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.ollama.api import pull_fetch_params, pull_fetch_by_index_params

__all__ = ["PullResource", "AsyncPullResource"]


class PullResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PullResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return PullResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PullResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/pyopenwebui-python#with_streaming_response
        """
        return PullResourceWithStreamingResponse(self)

    def fetch(
        self,
        *,
        name: str,
        url_idx: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Pull Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ollama/api/pull",
            body=maybe_transform({"name": name}, pull_fetch_params.PullFetchParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url_idx": url_idx}, pull_fetch_params.PullFetchParams),
            ),
            cast_to=object,
        )

    def fetch_by_index(
        self,
        url_idx: int,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Pull Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/ollama/api/pull/{url_idx}",
            body=maybe_transform({"name": name}, pull_fetch_by_index_params.PullFetchByIndexParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncPullResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPullResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPullResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPullResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/pyopenwebui-python#with_streaming_response
        """
        return AsyncPullResourceWithStreamingResponse(self)

    async def fetch(
        self,
        *,
        name: str,
        url_idx: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Pull Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ollama/api/pull",
            body=await async_maybe_transform({"name": name}, pull_fetch_params.PullFetchParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"url_idx": url_idx}, pull_fetch_params.PullFetchParams),
            ),
            cast_to=object,
        )

    async def fetch_by_index(
        self,
        url_idx: int,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Pull Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/ollama/api/pull/{url_idx}",
            body=await async_maybe_transform({"name": name}, pull_fetch_by_index_params.PullFetchByIndexParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class PullResourceWithRawResponse:
    def __init__(self, pull: PullResource) -> None:
        self._pull = pull

        self.fetch = to_raw_response_wrapper(
            pull.fetch,
        )
        self.fetch_by_index = to_raw_response_wrapper(
            pull.fetch_by_index,
        )


class AsyncPullResourceWithRawResponse:
    def __init__(self, pull: AsyncPullResource) -> None:
        self._pull = pull

        self.fetch = async_to_raw_response_wrapper(
            pull.fetch,
        )
        self.fetch_by_index = async_to_raw_response_wrapper(
            pull.fetch_by_index,
        )


class PullResourceWithStreamingResponse:
    def __init__(self, pull: PullResource) -> None:
        self._pull = pull

        self.fetch = to_streamed_response_wrapper(
            pull.fetch,
        )
        self.fetch_by_index = to_streamed_response_wrapper(
            pull.fetch_by_index,
        )


class AsyncPullResourceWithStreamingResponse:
    def __init__(self, pull: AsyncPullResource) -> None:
        self._pull = pull

        self.fetch = async_to_streamed_response_wrapper(
            pull.fetch,
        )
        self.fetch_by_index = async_to_streamed_response_wrapper(
            pull.fetch_by_index,
        )
