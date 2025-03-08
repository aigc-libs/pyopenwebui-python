# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional

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
from ....types.ollama.api import embed_create_params, embed_embed_model_params

__all__ = ["EmbedResource", "AsyncEmbedResource"]


class EmbedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmbedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return EmbedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmbedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/pyopenwebui-python#with_streaming_response
        """
        return EmbedResourceWithStreamingResponse(self)

    def create(
        self,
        url_idx: int,
        *,
        input: Union[List[str], str],
        model: str,
        keep_alive: Union[int, str, None] | NotGiven = NOT_GIVEN,
        options: Optional[object] | NotGiven = NOT_GIVEN,
        truncate: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Embed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/ollama/api/embed/{url_idx}",
            body=maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "keep_alive": keep_alive,
                    "options": options,
                    "truncate": truncate,
                },
                embed_create_params.EmbedCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def embed_model(
        self,
        *,
        input: Union[List[str], str],
        model: str,
        url_idx: Optional[int] | NotGiven = NOT_GIVEN,
        keep_alive: Union[int, str, None] | NotGiven = NOT_GIVEN,
        options: Optional[object] | NotGiven = NOT_GIVEN,
        truncate: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Embed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ollama/api/embed",
            body=maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "keep_alive": keep_alive,
                    "options": options,
                    "truncate": truncate,
                },
                embed_embed_model_params.EmbedEmbedModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url_idx": url_idx}, embed_embed_model_params.EmbedEmbedModelParams),
            ),
            cast_to=object,
        )


class AsyncEmbedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmbedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmbedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmbedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/pyopenwebui-python#with_streaming_response
        """
        return AsyncEmbedResourceWithStreamingResponse(self)

    async def create(
        self,
        url_idx: int,
        *,
        input: Union[List[str], str],
        model: str,
        keep_alive: Union[int, str, None] | NotGiven = NOT_GIVEN,
        options: Optional[object] | NotGiven = NOT_GIVEN,
        truncate: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Embed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/ollama/api/embed/{url_idx}",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "keep_alive": keep_alive,
                    "options": options,
                    "truncate": truncate,
                },
                embed_create_params.EmbedCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def embed_model(
        self,
        *,
        input: Union[List[str], str],
        model: str,
        url_idx: Optional[int] | NotGiven = NOT_GIVEN,
        keep_alive: Union[int, str, None] | NotGiven = NOT_GIVEN,
        options: Optional[object] | NotGiven = NOT_GIVEN,
        truncate: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Embed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ollama/api/embed",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "keep_alive": keep_alive,
                    "options": options,
                    "truncate": truncate,
                },
                embed_embed_model_params.EmbedEmbedModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"url_idx": url_idx}, embed_embed_model_params.EmbedEmbedModelParams),
            ),
            cast_to=object,
        )


class EmbedResourceWithRawResponse:
    def __init__(self, embed: EmbedResource) -> None:
        self._embed = embed

        self.create = to_raw_response_wrapper(
            embed.create,
        )
        self.embed_model = to_raw_response_wrapper(
            embed.embed_model,
        )


class AsyncEmbedResourceWithRawResponse:
    def __init__(self, embed: AsyncEmbedResource) -> None:
        self._embed = embed

        self.create = async_to_raw_response_wrapper(
            embed.create,
        )
        self.embed_model = async_to_raw_response_wrapper(
            embed.embed_model,
        )


class EmbedResourceWithStreamingResponse:
    def __init__(self, embed: EmbedResource) -> None:
        self._embed = embed

        self.create = to_streamed_response_wrapper(
            embed.create,
        )
        self.embed_model = to_streamed_response_wrapper(
            embed.embed_model,
        )


class AsyncEmbedResourceWithStreamingResponse:
    def __init__(self, embed: AsyncEmbedResource) -> None:
        self._embed = embed

        self.create = async_to_streamed_response_wrapper(
            embed.create,
        )
        self.embed_model = async_to_streamed_response_wrapper(
            embed.embed_model,
        )
