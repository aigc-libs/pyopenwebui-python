# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ....types.ollama.api import create_new_params, create_new_by_index_params

__all__ = ["CreateResource", "AsyncCreateResource"]


class CreateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return CreateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/pyopenwebui-python#with_streaming_response
        """
        return CreateResourceWithStreamingResponse(self)

    def new(
        self,
        *,
        url_idx: int | NotGiven = NOT_GIVEN,
        model: Optional[str] | NotGiven = NOT_GIVEN,
        path: Optional[str] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Create Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ollama/api/create",
            body=maybe_transform(
                {
                    "model": model,
                    "path": path,
                    "stream": stream,
                },
                create_new_params.CreateNewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url_idx": url_idx}, create_new_params.CreateNewParams),
            ),
            cast_to=object,
        )

    def new_by_index(
        self,
        url_idx: int,
        *,
        model: Optional[str] | NotGiven = NOT_GIVEN,
        path: Optional[str] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Create Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/ollama/api/create/{url_idx}",
            body=maybe_transform(
                {
                    "model": model,
                    "path": path,
                    "stream": stream,
                },
                create_new_by_index_params.CreateNewByIndexParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncCreateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCreateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCreateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/pyopenwebui-python#with_streaming_response
        """
        return AsyncCreateResourceWithStreamingResponse(self)

    async def new(
        self,
        *,
        url_idx: int | NotGiven = NOT_GIVEN,
        model: Optional[str] | NotGiven = NOT_GIVEN,
        path: Optional[str] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Create Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ollama/api/create",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "path": path,
                    "stream": stream,
                },
                create_new_params.CreateNewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"url_idx": url_idx}, create_new_params.CreateNewParams),
            ),
            cast_to=object,
        )

    async def new_by_index(
        self,
        url_idx: int,
        *,
        model: Optional[str] | NotGiven = NOT_GIVEN,
        path: Optional[str] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Create Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/ollama/api/create/{url_idx}",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "path": path,
                    "stream": stream,
                },
                create_new_by_index_params.CreateNewByIndexParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class CreateResourceWithRawResponse:
    def __init__(self, create: CreateResource) -> None:
        self._create = create

        self.new = to_raw_response_wrapper(
            create.new,
        )
        self.new_by_index = to_raw_response_wrapper(
            create.new_by_index,
        )


class AsyncCreateResourceWithRawResponse:
    def __init__(self, create: AsyncCreateResource) -> None:
        self._create = create

        self.new = async_to_raw_response_wrapper(
            create.new,
        )
        self.new_by_index = async_to_raw_response_wrapper(
            create.new_by_index,
        )


class CreateResourceWithStreamingResponse:
    def __init__(self, create: CreateResource) -> None:
        self._create = create

        self.new = to_streamed_response_wrapper(
            create.new,
        )
        self.new_by_index = to_streamed_response_wrapper(
            create.new_by_index,
        )


class AsyncCreateResourceWithStreamingResponse:
    def __init__(self, create: AsyncCreateResource) -> None:
        self._create = create

        self.new = async_to_streamed_response_wrapper(
            create.new,
        )
        self.new_by_index = async_to_streamed_response_wrapper(
            create.new_by_index,
        )
