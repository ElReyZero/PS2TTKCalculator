from ttk import getWeaponItem
import asyncio
from modules import config as cfg


async def main():
    gun, datasheet = await getWeaponItem(108, cfg.service_id)
    print(gun.name)
    print(datasheet)

if __name__ == '__main__':
    cfg.get_config()
    asyncio.get_event_loop().run_until_complete(main())