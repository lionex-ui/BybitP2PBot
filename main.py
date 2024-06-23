import os

import sys
import logging

import asyncio


from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

from bot.config import BotConfig

from bot.middleware.api import APIMiddleware
from bot.middleware.redis import RedisMiddleware
from bot.middleware.db import DbSessionMiddleware

from bot.handlers import auth

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


async def main():
    path = "//" + os.path.join(os.getcwd(), "users.db").replace("\\", "/").split(":/")[-1]
    engine = create_async_engine(f"sqlite+aiosqlite://{path}")
    async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

    bot = Bot(token=BotConfig.token.value, default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    ))
    dp = Dispatcher(bot=bot, storage=MemoryStorage())

    dp.update.middleware(APIMiddleware())
    dp.update.middleware(RedisMiddleware())
    dp.update.middleware(DbSessionMiddleware(session_pool=async_session_maker))

    dp.include_routers(
        auth.router
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
