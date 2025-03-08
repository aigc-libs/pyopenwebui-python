# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersion:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        version = client.api.version.get()
        assert_matches_type(object, version, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.version.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(object, version, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.version.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(object, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_latest_release(self, client: Pyopenwebui) -> None:
        version = client.api.version.get_latest_release()
        assert_matches_type(object, version, path=["response"])

    @parametrize
    def test_raw_response_get_latest_release(self, client: Pyopenwebui) -> None:
        response = client.api.version.with_raw_response.get_latest_release()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(object, version, path=["response"])

    @parametrize
    def test_streaming_response_get_latest_release(self, client: Pyopenwebui) -> None:
        with client.api.version.with_streaming_response.get_latest_release() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(object, version, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVersion:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        version = await async_client.api.version.get()
        assert_matches_type(object, version, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.version.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(object, version, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.version.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(object, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_latest_release(self, async_client: AsyncPyopenwebui) -> None:
        version = await async_client.api.version.get_latest_release()
        assert_matches_type(object, version, path=["response"])

    @parametrize
    async def test_raw_response_get_latest_release(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.version.with_raw_response.get_latest_release()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(object, version, path=["response"])

    @parametrize
    async def test_streaming_response_get_latest_release(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.version.with_streaming_response.get_latest_release() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(object, version, path=["response"])

        assert cast(Any, response.is_closed) is True
