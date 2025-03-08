# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1 import PromptModel
from pyopenwebui.types.api.v1.prompts import CommandDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCommand:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Pyopenwebui) -> None:
        command = client.api.v1.prompts.command.update(
            command_1="command",
            command_2="command",
            content="content",
            title="title",
        )
        assert_matches_type(Optional[PromptModel], command, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Pyopenwebui) -> None:
        command = client.api.v1.prompts.command.update(
            command_1="command",
            command_2="command",
            content="content",
            title="title",
            access_control={},
        )
        assert_matches_type(Optional[PromptModel], command, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Pyopenwebui) -> None:
        response = client.api.v1.prompts.command.with_raw_response.update(
            command_1="command",
            command_2="command",
            content="content",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = response.parse()
        assert_matches_type(Optional[PromptModel], command, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Pyopenwebui) -> None:
        with client.api.v1.prompts.command.with_streaming_response.update(
            command_1="command",
            command_2="command",
            content="content",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = response.parse()
            assert_matches_type(Optional[PromptModel], command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `command_1` but received ''"):
            client.api.v1.prompts.command.with_raw_response.update(
                command_1="",
                command_2="",
                content="content",
                title="title",
            )

    @parametrize
    def test_method_delete(self, client: Pyopenwebui) -> None:
        command = client.api.v1.prompts.command.delete(
            "command",
        )
        assert_matches_type(CommandDeleteResponse, command, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Pyopenwebui) -> None:
        response = client.api.v1.prompts.command.with_raw_response.delete(
            "command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = response.parse()
        assert_matches_type(CommandDeleteResponse, command, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Pyopenwebui) -> None:
        with client.api.v1.prompts.command.with_streaming_response.delete(
            "command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = response.parse()
            assert_matches_type(CommandDeleteResponse, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `command` but received ''"):
            client.api.v1.prompts.command.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        command = client.api.v1.prompts.command.get(
            "command",
        )
        assert_matches_type(Optional[PromptModel], command, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.prompts.command.with_raw_response.get(
            "command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = response.parse()
        assert_matches_type(Optional[PromptModel], command, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.prompts.command.with_streaming_response.get(
            "command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = response.parse()
            assert_matches_type(Optional[PromptModel], command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `command` but received ''"):
            client.api.v1.prompts.command.with_raw_response.get(
                "",
            )


class TestAsyncCommand:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncPyopenwebui) -> None:
        command = await async_client.api.v1.prompts.command.update(
            command_1="command",
            command_2="command",
            content="content",
            title="title",
        )
        assert_matches_type(Optional[PromptModel], command, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        command = await async_client.api.v1.prompts.command.update(
            command_1="command",
            command_2="command",
            content="content",
            title="title",
            access_control={},
        )
        assert_matches_type(Optional[PromptModel], command, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.prompts.command.with_raw_response.update(
            command_1="command",
            command_2="command",
            content="content",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = await response.parse()
        assert_matches_type(Optional[PromptModel], command, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.prompts.command.with_streaming_response.update(
            command_1="command",
            command_2="command",
            content="content",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = await response.parse()
            assert_matches_type(Optional[PromptModel], command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `command_1` but received ''"):
            await async_client.api.v1.prompts.command.with_raw_response.update(
                command_1="",
                command_2="",
                content="content",
                title="title",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncPyopenwebui) -> None:
        command = await async_client.api.v1.prompts.command.delete(
            "command",
        )
        assert_matches_type(CommandDeleteResponse, command, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.prompts.command.with_raw_response.delete(
            "command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = await response.parse()
        assert_matches_type(CommandDeleteResponse, command, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.prompts.command.with_streaming_response.delete(
            "command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = await response.parse()
            assert_matches_type(CommandDeleteResponse, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `command` but received ''"):
            await async_client.api.v1.prompts.command.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        command = await async_client.api.v1.prompts.command.get(
            "command",
        )
        assert_matches_type(Optional[PromptModel], command, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.prompts.command.with_raw_response.get(
            "command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = await response.parse()
        assert_matches_type(Optional[PromptModel], command, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.prompts.command.with_streaming_response.get(
            "command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = await response.parse()
            assert_matches_type(Optional[PromptModel], command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `command` but received ''"):
            await async_client.api.v1.prompts.command.with_raw_response.get(
                "",
            )
