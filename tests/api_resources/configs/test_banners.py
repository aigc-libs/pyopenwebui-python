# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.configs import BannerListResponse, BannerCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBanners:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Pyopenwebui) -> None:
        banner = client.configs.banners.create(
            banners=[
                {
                    "id": "id",
                    "content": "content",
                    "dismissible": True,
                    "timestamp": 0,
                    "type": "type",
                },
                {
                    "id": "id",
                    "content": "content",
                    "dismissible": True,
                    "timestamp": 0,
                    "type": "type",
                },
                {
                    "id": "id",
                    "content": "content",
                    "dismissible": True,
                    "timestamp": 0,
                    "type": "type",
                },
            ],
        )
        assert_matches_type(BannerCreateResponse, banner, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Pyopenwebui) -> None:
        response = client.configs.banners.with_raw_response.create(
            banners=[
                {
                    "id": "id",
                    "content": "content",
                    "dismissible": True,
                    "timestamp": 0,
                    "type": "type",
                },
                {
                    "id": "id",
                    "content": "content",
                    "dismissible": True,
                    "timestamp": 0,
                    "type": "type",
                },
                {
                    "id": "id",
                    "content": "content",
                    "dismissible": True,
                    "timestamp": 0,
                    "type": "type",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        banner = response.parse()
        assert_matches_type(BannerCreateResponse, banner, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Pyopenwebui) -> None:
        with client.configs.banners.with_streaming_response.create(
            banners=[
                {
                    "id": "id",
                    "content": "content",
                    "dismissible": True,
                    "timestamp": 0,
                    "type": "type",
                },
                {
                    "id": "id",
                    "content": "content",
                    "dismissible": True,
                    "timestamp": 0,
                    "type": "type",
                },
                {
                    "id": "id",
                    "content": "content",
                    "dismissible": True,
                    "timestamp": 0,
                    "type": "type",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            banner = response.parse()
            assert_matches_type(BannerCreateResponse, banner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Pyopenwebui) -> None:
        banner = client.configs.banners.list()
        assert_matches_type(BannerListResponse, banner, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Pyopenwebui) -> None:
        response = client.configs.banners.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        banner = response.parse()
        assert_matches_type(BannerListResponse, banner, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Pyopenwebui) -> None:
        with client.configs.banners.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            banner = response.parse()
            assert_matches_type(BannerListResponse, banner, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBanners:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPyopenwebui) -> None:
        banner = await async_client.configs.banners.create(
            banners=[
                {
                    "id": "id",
                    "content": "content",
                    "dismissible": True,
                    "timestamp": 0,
                    "type": "type",
                },
                {
                    "id": "id",
                    "content": "content",
                    "dismissible": True,
                    "timestamp": 0,
                    "type": "type",
                },
                {
                    "id": "id",
                    "content": "content",
                    "dismissible": True,
                    "timestamp": 0,
                    "type": "type",
                },
            ],
        )
        assert_matches_type(BannerCreateResponse, banner, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.configs.banners.with_raw_response.create(
            banners=[
                {
                    "id": "id",
                    "content": "content",
                    "dismissible": True,
                    "timestamp": 0,
                    "type": "type",
                },
                {
                    "id": "id",
                    "content": "content",
                    "dismissible": True,
                    "timestamp": 0,
                    "type": "type",
                },
                {
                    "id": "id",
                    "content": "content",
                    "dismissible": True,
                    "timestamp": 0,
                    "type": "type",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        banner = await response.parse()
        assert_matches_type(BannerCreateResponse, banner, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.configs.banners.with_streaming_response.create(
            banners=[
                {
                    "id": "id",
                    "content": "content",
                    "dismissible": True,
                    "timestamp": 0,
                    "type": "type",
                },
                {
                    "id": "id",
                    "content": "content",
                    "dismissible": True,
                    "timestamp": 0,
                    "type": "type",
                },
                {
                    "id": "id",
                    "content": "content",
                    "dismissible": True,
                    "timestamp": 0,
                    "type": "type",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            banner = await response.parse()
            assert_matches_type(BannerCreateResponse, banner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncPyopenwebui) -> None:
        banner = await async_client.configs.banners.list()
        assert_matches_type(BannerListResponse, banner, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.configs.banners.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        banner = await response.parse()
        assert_matches_type(BannerListResponse, banner, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.configs.banners.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            banner = await response.parse()
            assert_matches_type(BannerListResponse, banner, path=["response"])

        assert cast(Any, response.is_closed) is True
