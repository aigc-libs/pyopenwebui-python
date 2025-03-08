# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_tag(self, client: Pyopenwebui) -> None:
        tag = client.ollama.api.tags.get_tag(
            0,
        )
        assert_matches_type(object, tag, path=["response"])

    @parametrize
    def test_raw_response_get_tag(self, client: Pyopenwebui) -> None:
        response = client.ollama.api.tags.with_raw_response.get_tag(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(object, tag, path=["response"])

    @parametrize
    def test_streaming_response_get_tag(self, client: Pyopenwebui) -> None:
        with client.ollama.api.tags.with_streaming_response.get_tag(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(object, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_tags(self, client: Pyopenwebui) -> None:
        tag = client.ollama.api.tags.list_tags()
        assert_matches_type(object, tag, path=["response"])

    @parametrize
    def test_method_list_tags_with_all_params(self, client: Pyopenwebui) -> None:
        tag = client.ollama.api.tags.list_tags(
            url_idx=0,
        )
        assert_matches_type(object, tag, path=["response"])

    @parametrize
    def test_raw_response_list_tags(self, client: Pyopenwebui) -> None:
        response = client.ollama.api.tags.with_raw_response.list_tags()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(object, tag, path=["response"])

    @parametrize
    def test_streaming_response_list_tags(self, client: Pyopenwebui) -> None:
        with client.ollama.api.tags.with_streaming_response.list_tags() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(object, tag, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTags:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_tag(self, async_client: AsyncPyopenwebui) -> None:
        tag = await async_client.ollama.api.tags.get_tag(
            0,
        )
        assert_matches_type(object, tag, path=["response"])

    @parametrize
    async def test_raw_response_get_tag(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.api.tags.with_raw_response.get_tag(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(object, tag, path=["response"])

    @parametrize
    async def test_streaming_response_get_tag(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.api.tags.with_streaming_response.get_tag(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(object, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_tags(self, async_client: AsyncPyopenwebui) -> None:
        tag = await async_client.ollama.api.tags.list_tags()
        assert_matches_type(object, tag, path=["response"])

    @parametrize
    async def test_method_list_tags_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        tag = await async_client.ollama.api.tags.list_tags(
            url_idx=0,
        )
        assert_matches_type(object, tag, path=["response"])

    @parametrize
    async def test_raw_response_list_tags(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.api.tags.with_raw_response.list_tags()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(object, tag, path=["response"])

    @parametrize
    async def test_streaming_response_list_tags(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.api.tags.with_streaming_response.list_tags() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(object, tag, path=["response"])

        assert cast(Any, response.is_closed) is True
