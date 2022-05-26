import asyncio
from auraxium import ps2, Client

loop = asyncio.get_event_loop()

async def getWeaponItem(item_id:int, service_id:str):
    """Get a weapon item from the API.

        :param item_id: The item ID of the weapon.
        :param service_id: The Census API service ID to use.

        :returns: A tuple containing the weapon item and its datasheet.
    """
    async with Client(service_id=service_id) as client:
        gun = await client.get_by_id(ps2.Weapon, item_id)
        item = await gun.item().resolve()
        datasheet = await gun.datasheet()
        return item, datasheet

