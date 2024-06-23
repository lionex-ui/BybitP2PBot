from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from bot.redis import Redis


class RedisMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
        self.redis = Redis()

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:

        data["redis"] = self.redis
        return await handler(event, data)
