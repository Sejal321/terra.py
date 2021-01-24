from ._base import BaseAPI

from typing import Optional


class TendermintAPI(BaseAPI):
    async def node_info(self) -> dict:
        return await self._c._get("/node_info")

    async def syncing(self) -> bool:
        return await self._c._get("/syncing")

    async def validator_set(self, height: Optional[int] = None) -> dict:
        x = "latest" if height is None else height
        return (await self._c._get(f"/validatorsets/{x}"))["result"]

    async def block_info(self, height: Optional[int] = None) -> dict:
        x = "latest" if height is None else height
        return await self._c._get(f"/blocks/{x}")
