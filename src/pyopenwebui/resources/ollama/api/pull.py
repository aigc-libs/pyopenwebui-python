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
from ....types.ollama.api import pull_create_params, pull_pull_model_params

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

    def create(
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
            body=maybe_transform({"name": name}, pull_create_params.PullCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def pull_model(
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
            body=maybe_transform({"name": name}, pull_pull_model_params.PullPullModelParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url_idx": url_idx}, pull_pull_model_params.PullPullModelParams),
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

    async def create(
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
            body=await async_maybe_transform({"name": name}, pull_create_params.PullCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def pull_model(
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
            body=await async_maybe_transform({"name": name}, pull_pull_model_params.PullPullModelParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"url_idx": url_idx}, pull_pull_model_params.PullPullModelParams),
            ),
            cast_to=object,
        )


class PullResourceWithRawResponse:
    def __init__(self, pull: PullResource) -> None:
        self._pull = pull

        self.create = to_raw_response_wrapper(
            pull.create,
        )
        self.pull_model = to_raw_response_wrapper(
            pull.pull_model,
        )


class AsyncPullResourceWithRawResponse:
    def __init__(self, pull: AsyncPullResource) -> None:
        self._pull = pull

        self.create = async_to_raw_response_wrapper(
            pull.create,
        )
        self.pull_model = async_to_raw_response_wrapper(
            pull.pull_model,
        )


class PullResourceWithStreamingResponse:
    def __init__(self, pull: PullResource) -> None:
        self._pull = pull

        self.create = to_streamed_response_wrapper(
            pull.create,
        )
        self.pull_model = to_streamed_response_wrapper(
            pull.pull_model,
        )


class AsyncPullResourceWithStreamingResponse:
    def __init__(self, pull: AsyncPullResource) -> None:
        self._pull = pull

        self.create = async_to_streamed_response_wrapper(
            pull.create,
        )
        self.pull_model = async_to_streamed_response_wrapper(
            pull.pull_model,
        )
