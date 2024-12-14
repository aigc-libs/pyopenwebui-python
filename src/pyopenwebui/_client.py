# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import root, models
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.auths import auths
from .resources.chats import chats
from .resources.files import files
from .resources.tools import tools
from .resources.users import users
from .resources.utils import utils
from .resources.configs import configs
from .resources.prompts import prompts
from .resources.memories import memories
from .resources.documents import documents
from .resources.functions import functions

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Pyopenwebui",
    "AsyncPyopenwebui",
    "Client",
    "AsyncClient",
]


class Pyopenwebui(SyncAPIClient):
    configs: configs.ConfigsResource
    auths: auths.AuthsResource
    users: users.UsersResource
    chats: chats.ChatsResource
    documents: documents.DocumentsResource
    models: models.ModelsResource
    prompts: prompts.PromptsResource
    memories: memories.MemoriesResource
    files: files.FilesResource
    tools: tools.ToolsResource
    functions: functions.FunctionsResource
    utils: utils.UtilsResource
    root: root.RootResource
    with_raw_response: PyopenwebuiWithRawResponse
    with_streaming_response: PyopenwebuiWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous pyopenwebui client instance."""
        if base_url is None:
            base_url = os.environ.get("PYOPENWEBUI_BASE_URL")
        if base_url is None:
            base_url = f"/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.configs = configs.ConfigsResource(self)
        self.auths = auths.AuthsResource(self)
        self.users = users.UsersResource(self)
        self.chats = chats.ChatsResource(self)
        self.documents = documents.DocumentsResource(self)
        self.models = models.ModelsResource(self)
        self.prompts = prompts.PromptsResource(self)
        self.memories = memories.MemoriesResource(self)
        self.files = files.FilesResource(self)
        self.tools = tools.ToolsResource(self)
        self.functions = functions.FunctionsResource(self)
        self.utils = utils.UtilsResource(self)
        self.root = root.RootResource(self)
        self.with_raw_response = PyopenwebuiWithRawResponse(self)
        self.with_streaming_response = PyopenwebuiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncPyopenwebui(AsyncAPIClient):
    configs: configs.AsyncConfigsResource
    auths: auths.AsyncAuthsResource
    users: users.AsyncUsersResource
    chats: chats.AsyncChatsResource
    documents: documents.AsyncDocumentsResource
    models: models.AsyncModelsResource
    prompts: prompts.AsyncPromptsResource
    memories: memories.AsyncMemoriesResource
    files: files.AsyncFilesResource
    tools: tools.AsyncToolsResource
    functions: functions.AsyncFunctionsResource
    utils: utils.AsyncUtilsResource
    root: root.AsyncRootResource
    with_raw_response: AsyncPyopenwebuiWithRawResponse
    with_streaming_response: AsyncPyopenwebuiWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async pyopenwebui client instance."""
        if base_url is None:
            base_url = os.environ.get("PYOPENWEBUI_BASE_URL")
        if base_url is None:
            base_url = f"/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.configs = configs.AsyncConfigsResource(self)
        self.auths = auths.AsyncAuthsResource(self)
        self.users = users.AsyncUsersResource(self)
        self.chats = chats.AsyncChatsResource(self)
        self.documents = documents.AsyncDocumentsResource(self)
        self.models = models.AsyncModelsResource(self)
        self.prompts = prompts.AsyncPromptsResource(self)
        self.memories = memories.AsyncMemoriesResource(self)
        self.files = files.AsyncFilesResource(self)
        self.tools = tools.AsyncToolsResource(self)
        self.functions = functions.AsyncFunctionsResource(self)
        self.utils = utils.AsyncUtilsResource(self)
        self.root = root.AsyncRootResource(self)
        self.with_raw_response = AsyncPyopenwebuiWithRawResponse(self)
        self.with_streaming_response = AsyncPyopenwebuiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class PyopenwebuiWithRawResponse:
    def __init__(self, client: Pyopenwebui) -> None:
        self.configs = configs.ConfigsResourceWithRawResponse(client.configs)
        self.auths = auths.AuthsResourceWithRawResponse(client.auths)
        self.users = users.UsersResourceWithRawResponse(client.users)
        self.chats = chats.ChatsResourceWithRawResponse(client.chats)
        self.documents = documents.DocumentsResourceWithRawResponse(client.documents)
        self.models = models.ModelsResourceWithRawResponse(client.models)
        self.prompts = prompts.PromptsResourceWithRawResponse(client.prompts)
        self.memories = memories.MemoriesResourceWithRawResponse(client.memories)
        self.files = files.FilesResourceWithRawResponse(client.files)
        self.tools = tools.ToolsResourceWithRawResponse(client.tools)
        self.functions = functions.FunctionsResourceWithRawResponse(client.functions)
        self.utils = utils.UtilsResourceWithRawResponse(client.utils)
        self.root = root.RootResourceWithRawResponse(client.root)


class AsyncPyopenwebuiWithRawResponse:
    def __init__(self, client: AsyncPyopenwebui) -> None:
        self.configs = configs.AsyncConfigsResourceWithRawResponse(client.configs)
        self.auths = auths.AsyncAuthsResourceWithRawResponse(client.auths)
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)
        self.chats = chats.AsyncChatsResourceWithRawResponse(client.chats)
        self.documents = documents.AsyncDocumentsResourceWithRawResponse(client.documents)
        self.models = models.AsyncModelsResourceWithRawResponse(client.models)
        self.prompts = prompts.AsyncPromptsResourceWithRawResponse(client.prompts)
        self.memories = memories.AsyncMemoriesResourceWithRawResponse(client.memories)
        self.files = files.AsyncFilesResourceWithRawResponse(client.files)
        self.tools = tools.AsyncToolsResourceWithRawResponse(client.tools)
        self.functions = functions.AsyncFunctionsResourceWithRawResponse(client.functions)
        self.utils = utils.AsyncUtilsResourceWithRawResponse(client.utils)
        self.root = root.AsyncRootResourceWithRawResponse(client.root)


class PyopenwebuiWithStreamedResponse:
    def __init__(self, client: Pyopenwebui) -> None:
        self.configs = configs.ConfigsResourceWithStreamingResponse(client.configs)
        self.auths = auths.AuthsResourceWithStreamingResponse(client.auths)
        self.users = users.UsersResourceWithStreamingResponse(client.users)
        self.chats = chats.ChatsResourceWithStreamingResponse(client.chats)
        self.documents = documents.DocumentsResourceWithStreamingResponse(client.documents)
        self.models = models.ModelsResourceWithStreamingResponse(client.models)
        self.prompts = prompts.PromptsResourceWithStreamingResponse(client.prompts)
        self.memories = memories.MemoriesResourceWithStreamingResponse(client.memories)
        self.files = files.FilesResourceWithStreamingResponse(client.files)
        self.tools = tools.ToolsResourceWithStreamingResponse(client.tools)
        self.functions = functions.FunctionsResourceWithStreamingResponse(client.functions)
        self.utils = utils.UtilsResourceWithStreamingResponse(client.utils)
        self.root = root.RootResourceWithStreamingResponse(client.root)


class AsyncPyopenwebuiWithStreamedResponse:
    def __init__(self, client: AsyncPyopenwebui) -> None:
        self.configs = configs.AsyncConfigsResourceWithStreamingResponse(client.configs)
        self.auths = auths.AsyncAuthsResourceWithStreamingResponse(client.auths)
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)
        self.chats = chats.AsyncChatsResourceWithStreamingResponse(client.chats)
        self.documents = documents.AsyncDocumentsResourceWithStreamingResponse(client.documents)
        self.models = models.AsyncModelsResourceWithStreamingResponse(client.models)
        self.prompts = prompts.AsyncPromptsResourceWithStreamingResponse(client.prompts)
        self.memories = memories.AsyncMemoriesResourceWithStreamingResponse(client.memories)
        self.files = files.AsyncFilesResourceWithStreamingResponse(client.files)
        self.tools = tools.AsyncToolsResourceWithStreamingResponse(client.tools)
        self.functions = functions.AsyncFunctionsResourceWithStreamingResponse(client.functions)
        self.utils = utils.AsyncUtilsResourceWithStreamingResponse(client.utils)
        self.root = root.AsyncRootResourceWithStreamingResponse(client.root)


Client = Pyopenwebui

AsyncClient = AsyncPyopenwebui
