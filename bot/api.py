import asyncio
import aiohttp

from typing import List

from bot.schemas import Orders


class API:

    def __init__(self):
        self._api_url = "https://api2.bybit.com"

    @staticmethod
    async def get_matching_orders(
            *,
            orders: Orders.RequestResponse,
            order_num: int
    ) -> List[Orders.ItemResponse]:

        matching_orders: List[Orders.ItemResponse] = []
        items = orders["result"]["items"]

        for item in items:
            if int(item["recentOrderNum"] >= order_num):
                matching_orders.append(item)

        return matching_orders

    @staticmethod
    async def get_orders(
            *,
            url: str,
            json: Orders.RequestJson,
            session: aiohttp.ClientSession
    ) -> Orders.RequestResponse:

        response = await session.request(
            method="POST",
            url=url,
            json=json
        )
        result: Orders.RequestResponse = await response.json()

        return result

    async def get_actual_orders(
            self,
            *,
            user_id: int,
            token_id: str,
            currencies: List[str],
            payment: List[str],
            amount: str
    ) -> Orders.RequestResponse:

        tasks = []

        url: str = self._api_url + "/fiat/otc/item/online"
        json: Orders.RequestJson = {
            "userId": user_id,
            "tokenId": token_id,
            "payment": payment,
            "amount": amount,
            "authMaker": False,
            "canTrade": False,
            "side": "0",
            "size": "100",
            "page": "1"
        }

        session = aiohttp.ClientSession()

        for currency_id in currencies:
            json["currencyId"] = currency_id
            tasks.append(
                self.get_orders(
                    url=url,
                    json=json,
                    session=session
                )
            )
        results: List[Orders.RequestResponse] = await asyncio.gather(*tasks)

        await session.close()

        total_counts = sum([result["result"]["count"] for result in results])
        final_result: Orders.RequestResponse = {
            "ret_code": 0,
            "ret_msg": results[0]["ret_msg"],
            "result": {
                "count": total_counts,
                "items": []
            }
        }

        for result in results:
            final_result["result"]["items"].extend(result["result"]["items"])

        return final_result
