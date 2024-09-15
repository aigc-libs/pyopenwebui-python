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
from ....types.user_model import UserModel
from ....types.users.update import role_create_params

__all__ = ["RoleResource", "AsyncRoleResource"]


class RoleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return RoleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return RoleResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        role: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UserModel]:
        """
        Update User Role

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/users/update/role",
            body=maybe_transform(
                {
                    "id": id,
                    "role": role,
                },
                role_create_params.RoleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserModel,
        )


class AsyncRoleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncRoleResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        role: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UserModel]:
        """
        Update User Role

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/users/update/role",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "role": role,
                },
                role_create_params.RoleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserModel,
        )


class RoleResourceWithRawResponse:
    def __init__(self, role: RoleResource) -> None:
        self._role = role

        self.create = to_raw_response_wrapper(
            role.create,
        )


class AsyncRoleResourceWithRawResponse:
    def __init__(self, role: AsyncRoleResource) -> None:
        self._role = role

        self.create = async_to_raw_response_wrapper(
            role.create,
        )


class RoleResourceWithStreamingResponse:
    def __init__(self, role: RoleResource) -> None:
        self._role = role

        self.create = to_streamed_response_wrapper(
            role.create,
        )


class AsyncRoleResourceWithStreamingResponse:
    def __init__(self, role: AsyncRoleResource) -> None:
        self._role = role

        self.create = async_to_streamed_response_wrapper(
            role.create,
        )
