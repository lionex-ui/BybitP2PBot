import json
from typing import List

import aioredis

from bot.config import RedisConfig


class Redis:

    def __init__(self):
        self._redis = aioredis.from_url(RedisConfig().get_connection_string())

    async def get_orders(
            self
    ) -> List[int]:

        return json.loads(await self._redis.get("saved_orders"))

    async def save_orders(
            self,
            *,
            saved_orders: List[int]
    ) -> None:

        await self._redis.setnx("saved_orders", json.dumps(saved_orders))

    async def check_if_exists(
            self,
            *,
            orders: List[int]
    ) -> List[int]:

        saved_orders = await self.get_orders()
        new_orders = []

        for order in orders:
            if order not in saved_orders:
                new_orders.append(order)
                saved_orders.append(order)

        await self.save_orders(
            saved_orders=saved_orders
        )

        await self._redis.save()

        return new_orders
