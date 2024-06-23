from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from bot.api import API


class APIMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
        self.api = API()

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:

        data["api"] = self.api
        return await handler(event, data)
