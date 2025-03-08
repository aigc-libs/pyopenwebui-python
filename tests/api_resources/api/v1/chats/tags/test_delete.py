# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1.chats.tags import DeleteAllResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDelete:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_all(self, client: Pyopenwebui) -> None:
        delete = client.api.v1.chats.tags.delete.all(
            "id",
        )
        assert_matches_type(Optional[DeleteAllResponse], delete, path=["response"])

    @parametrize
    def test_raw_response_all(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.tags.delete.with_raw_response.all(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delete = response.parse()
        assert_matches_type(Optional[DeleteAllResponse], delete, path=["response"])

    @parametrize
    def test_streaming_response_all(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.tags.delete.with_streaming_response.all(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delete = response.parse()
            assert_matches_type(Optional[DeleteAllResponse], delete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_all(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.chats.tags.delete.with_raw_response.all(
                "",
            )


class TestAsyncDelete:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_all(self, async_client: AsyncPyopenwebui) -> None:
        delete = await async_client.api.v1.chats.tags.delete.all(
            "id",
        )
        assert_matches_type(Optional[DeleteAllResponse], delete, path=["response"])

    @parametrize
    async def test_raw_response_all(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.tags.delete.with_raw_response.all(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delete = await response.parse()
        assert_matches_type(Optional[DeleteAllResponse], delete, path=["response"])

    @parametrize
    async def test_streaming_response_all(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.tags.delete.with_streaming_response.all(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delete = await response.parse()
            assert_matches_type(Optional[DeleteAllResponse], delete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_all(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.chats.tags.delete.with_raw_response.all(
                "",
            )
