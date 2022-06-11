"""
| Script for populating the weapon database.
| Tools for interacting with weapons listed in the census API
"""

# External imports
import requests
import json

# Internal imports
import modules.config as cfg
from .models import Weapon
from .database import save_weapons_to_db
item_type_id = 26  # weapon

# List of all categories
we_cats = {
    2: 'Knife',  
    3: 'Pistol',  
    8: 'Carbine',  
    7: 'Assault Rifle',
    4: 'Shotgun',  
    6: 'LMG',  
    13: 'Rocket Launcher',
    11: 'Sniper Rifle',  
    18: 'Explosive', 
    5: 'SMG',  
    19: 'Battle Rifle',  
    24: 'Crossbow',  
    12: 'Scout Rifle',  
    10: 'AI MAX (Left)',  
    14: 'Heavy Weapon',  
    21: 'AV MAX (Right)',  
    20: 'AA MAX (Right)',  
    22: 'AI MAX (Right)',  
    9: 'AV MAX (Left)',  
    23: 'AA MAX (Left)',  
    147: 'Aerial Combat Weapon',
    104: 'Vehicle Weapons',  
    211: 'Colossus Primary Weapon',  
    144: 'ANT Top Turret',  
    157: 'Hybrid Rifle',  
    126: 'Reaver Wing Mount' 
}


def get_unknown_weapon():
    n_data = dict()
    n_data["id"] = 0
    n_data["name"] = "Unknown"
    n_data["faction"] = 0
    n_data["category_id"] = 0
    n_data["muzzle_velocity"] = 0
    n_data["refire_ms"] = 0
    n_data["max_damage"] = 0
    n_data["min_damage"] = 0
    n_data["damage_max_range"] = 0
    n_data["damage_min_range"] = 0
    n_data["image_link"] = None
    return n_data


def push_all_weapons(push_db=False):
    giga_list = list()
    for cat in we_cats.keys():

        #Get all weapons from the category
        url = f'http://census.daybreakgames.com/{cfg.service_id}/get/ps2:v2/item/' \
              f'?item_type_id=26&is_vehicle_weapon=0&item_category_id={cat}' \
              f'&c:limit=5000&c:show=item_id,item_category_id,name.en,faction_id,image_id&c:join=weapon_datasheet^inject_at:weapon.datasheet,fire_mode'
        response = requests.get(url)
        j_data = json.loads(response.content)
        print(we_cats[cat])  # Print category name

        print(url)
        if "returned" not in j_data:
            raise ValueError("Nothing returned!")
        if j_data["returned"] == 0:
            raise ValueError("Nothing returned!")

        # Iterate trough weapons of this category
        for we in j_data["item_list"]:
            n_data = dict()
            n_data["id"] = int(we["item_id"])  # Weapon ID
            if n_data["id"] == 0:
                raise ValueError("ID = 0")
            try:
                n_data["name"] = we["name"]["en"]  # Weapon name
            except KeyError:
                n_data["name"] = "Unknown"
                print("Unknown weapon, id: " + we["item_id"])
            try:
                n_data["faction"] = int(we["faction_id"])  # Get weapon's faction
            except KeyError:
                n_data["faction"] = 0
            n_data["category_id"] = int(we["item_category_id"])  # Weapon category
            try:
                n_data["muzzle_velocity"] = int(we['item_id_join_fire_mode']['muzzle_velocity'])
            except KeyError:
                n_data["muzzle_velocity"] = 0
            try:
                n_data["refire_ms"] = int(we['weapon']['datasheet']['fire_rate_ms'])
            except KeyError:
                n_data["refire_ms"] = 0
            try:
                n_data["max_damage"] = int(we['item_id_join_fire_mode']['damage_max'])
            except KeyError:
                n_data["max_damage"] = 0
            try:
                n_data["min_damage"] = int(we['item_id_join_fire_mode']['damage_min'])
            except KeyError:
                n_data["min_damage"] = 0
            try:
                n_data["damage_max_range"] = int(we['item_id_join_fire_mode']['damage_max_range'])
            except KeyError:
                n_data["damage_max_range"] = 0
            try:
                n_data["damage_min_range"] = int(we['item_id_join_fire_mode']['damage_min_range'])
            except KeyError:
                n_data["damage_min_range"] = 0
            try:
                n_data["image_link"] = f"https://census.daybreakgames.com/files/ps2/images/static/{we['image_id']}.png"
            except KeyError:
                n_data["image_link"] = None

            giga_list.append(n_data)
            # Find weapons new to database:
            try:
                Weapon.objects.get(id=n_data["id"])
            except Weapon.DoesNotExist:
                print(f'Weapon not found in database: '
                      f'cat : {n_data["category_id"]}, name: {n_data["name"]}, id: {n_data["id"]}')

    # Add the unknown weapon to the list
    giga_list.append(get_unknown_weapon())
    if push_db:
        save_weapons_to_db(giga_list)
        print("DB updated!")
        return giga_list
    else:
        print("DB not updated! Use arg 'push_db=True' to update")


def display_weapons_from_category(cat):
    url = f'http://census.daybreakgames.com/{cfg.service_id}/get/ps2:v2/item/' \
          f'?item_type_id=26&is_vehicle_weapon=0&item_category_id={cat}' \
          f'&c:limit=5000&c:show=item_id,item_category_id,name.en,faction_id'
    response = requests.get(url)
    j_data = json.loads(response.content)
    if j_data["returned"] == 0:
        print("Error")
        return
    for we in j_data["item_list"]:
        print(f"{we['item_id']};{we['name']['en']}")


def get_all_categories():
    url = f'http://census.daybreakgames.com/{cfg.service_id}/get/ps2:v2/item_category/?c:limit=500'
    response = requests.get(url)
    j_data = json.loads(response.content)

    if j_data["returned"] == 0:
        print("Error")
        return

    di = dict()
    for cat in j_data["item_category_list"]:
        di[int(cat["item_category_id"])] = cat["name"]["en"]
    return di


def get_weapons_categories():
    url = f'http://census.daybreakgames.com/{cfg.service_id}/get/ps2:v2/item/' \
          f'?item_type_id=26&is_vehicle_weapon=0&c:limit=5000' \
          f'&c:show=item_id,item_category_id,name.en'
    response = requests.get(url)
    j_data = json.loads(response.content)
    if j_data["returned"] == 0:
        print("Error")
        return
    cats = list()

    for we in j_data["item_list"]:
        we["id"] = int(we.pop("item_id"))
        try:
            we["name"] = we.pop("name")["en"]
        except KeyError:
            print(f'KeyError on name of id {we["id"]}')
        try:
            we["cat_id"] = int(we.pop("item_category_id"))
            if we["cat_id"] not in cats:
                cats.append(we["cat_id"])
        except KeyError:
            print(f'KeyError on cat of id {we["id"]}')

    return cats
