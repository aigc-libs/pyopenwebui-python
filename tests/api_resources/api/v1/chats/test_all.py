# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1.chats import AllDBResponse, AllTagsResponse, AllArchivedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAll:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_archived(self, client: Pyopenwebui) -> None:
        all = client.api.v1.chats.all.archived()
        assert_matches_type(AllArchivedResponse, all, path=["response"])

    @parametrize
    def test_raw_response_archived(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.all.with_raw_response.archived()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        all = response.parse()
        assert_matches_type(AllArchivedResponse, all, path=["response"])

    @parametrize
    def test_streaming_response_archived(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.all.with_streaming_response.archived() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            all = response.parse()
            assert_matches_type(AllArchivedResponse, all, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_db(self, client: Pyopenwebui) -> None:
        all = client.api.v1.chats.all.db()
        assert_matches_type(AllDBResponse, all, path=["response"])

    @parametrize
    def test_raw_response_db(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.all.with_raw_response.db()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        all = response.parse()
        assert_matches_type(AllDBResponse, all, path=["response"])

    @parametrize
    def test_streaming_response_db(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.all.with_streaming_response.db() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            all = response.parse()
            assert_matches_type(AllDBResponse, all, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tags(self, client: Pyopenwebui) -> None:
        all = client.api.v1.chats.all.tags()
        assert_matches_type(AllTagsResponse, all, path=["response"])

    @parametrize
    def test_raw_response_tags(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.all.with_raw_response.tags()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        all = response.parse()
        assert_matches_type(AllTagsResponse, all, path=["response"])

    @parametrize
    def test_streaming_response_tags(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.all.with_streaming_response.tags() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            all = response.parse()
            assert_matches_type(AllTagsResponse, all, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAll:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_archived(self, async_client: AsyncPyopenwebui) -> None:
        all = await async_client.api.v1.chats.all.archived()
        assert_matches_type(AllArchivedResponse, all, path=["response"])

    @parametrize
    async def test_raw_response_archived(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.all.with_raw_response.archived()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        all = await response.parse()
        assert_matches_type(AllArchivedResponse, all, path=["response"])

    @parametrize
    async def test_streaming_response_archived(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.all.with_streaming_response.archived() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            all = await response.parse()
            assert_matches_type(AllArchivedResponse, all, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_db(self, async_client: AsyncPyopenwebui) -> None:
        all = await async_client.api.v1.chats.all.db()
        assert_matches_type(AllDBResponse, all, path=["response"])

    @parametrize
    async def test_raw_response_db(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.all.with_raw_response.db()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        all = await response.parse()
        assert_matches_type(AllDBResponse, all, path=["response"])

    @parametrize
    async def test_streaming_response_db(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.all.with_streaming_response.db() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            all = await response.parse()
            assert_matches_type(AllDBResponse, all, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tags(self, async_client: AsyncPyopenwebui) -> None:
        all = await async_client.api.v1.chats.all.tags()
        assert_matches_type(AllTagsResponse, all, path=["response"])

    @parametrize
    async def test_raw_response_tags(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.all.with_raw_response.tags()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        all = await response.parse()
        assert_matches_type(AllTagsResponse, all, path=["response"])

    @parametrize
    async def test_streaming_response_tags(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.all.with_streaming_response.tags() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            all = await response.parse()
            assert_matches_type(AllTagsResponse, all, path=["response"])

        assert cast(Any, response.is_closed) is True
