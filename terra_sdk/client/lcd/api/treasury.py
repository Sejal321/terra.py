from ._base import BaseAPI

from terra_sdk.core.coin import Coin
from terra_sdk.core.dec import Dec


class TreasuryAPI(BaseAPI):
    async def tax_cap(self, denom: str) -> Coin:
        res = await self._c._get(f"/treasury/tax_cap/{denom}")
        return Coin(denom, res["result"])

    async def tax_rate(self) -> Dec:
        res = await self._c._get(f"/treasury/tax_rate")
        return Dec(res["result"])

    async def reward_weight(self) -> Dec:
        res = await self._c._get(f"/treasury/reward_weight")
        return Dec(res["result"])

    async def tax_proceeds(self) -> Coins:
        res = await self._c._get(f"/treasury/tax_proceeds")
        return Coins.from_data(res["result"])

    async def seigniorage_proceeds(self) -> Coin:
        res = await self._c._get(f"/treasury/seigniorage_proceeds")
        return Coin("uluna", res["result"])

    async def parameters(self) -> Coin:
        res = await self._c._get(f"/treasury/paramters")
        return res["result"]
