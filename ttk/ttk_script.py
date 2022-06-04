from auraxium import census
import modules.config as cfg
import requests

from modules.config import MissingConfig

def getWeaponItemUrl(weapon_name:str)->tuple:
    """Get a weapon item url from the API.

        Args:
        weapon_nam,e (str): The item ID of the weapon.
        Returns:
            tuple: A tuple containing the weapon item and its datasheet.
    """
    if cfg.service_id == "s:":
        raise MissingConfig("service_id")
        
    query = census.Query('item', service_id=cfg.service_id)
    query.add_term('name.en', weapon_name)
    query.create_join('weapon_datasheet')
    url = str(query.url()) + "^inject_at:weapon.datasheet,fire_mode"
    return url

def calculateTTK(refire_ms:float, shots:int, distance:float, velocity:float)->float:
    """Calculate the time to kill for a weapon.

        Args:
            refire_ms (float): The weapon's refire rate in milliseconds.
            shots (int): The number of shots to fire.
            distance (float): The distance to the target.
            velocity (float): The weapon's muzzle velocity in (m/s).
        Returns:
            float: The time to kill in seconds.
    """
    return (refire_ms/1000)*(shots-1) + distance/velocity


def getTTK(weapon_name:str, shots:int, distance:float):
    """Get the time to kill for a weapon.
        Args:
            weapon_name (str): The weapon's name.
            shots (int): The number of shots to fire.
            distance (float): The distance to the target.
        Returns:
            float: The time to kill in seconds.
    """

    url = getWeaponItemUrl(weapon_name)
    data = requests.get(url)
    try:
        weapon_data = data.json()['item_list'][0] 
        muzzle_velocity = int(weapon_data['item_id_join_fire_mode']['muzzle_velocity'])
        refire_ms = int(weapon_data['weapon']['datasheet']['fire_rate_ms'])
        ttk = calculateTTK(refire_ms, shots, distance, muzzle_velocity)
        return ttk
    except IndexError:
        return "Weapon not found."


def getConfig():
    cfg.get_config()
