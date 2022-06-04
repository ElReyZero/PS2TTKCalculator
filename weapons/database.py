from .models import Weapon

def save_weapons_to_db(weapon_list):
    weapons = list()
    for weapon in weapon_list:
        try:
            Weapon.objects.get(id=weapon["id"])
        except Weapon.DoesNotExist:
            new_weapon = Weapon(
                id=weapon["id"],
                name=weapon["name"],
                faction=weapon["faction"],
                category_id=weapon["category_id"],
                muzzle_velocity=weapon["muzzle_velocity"],
                refire_ms=weapon["refire_ms"],
                max_damage=weapon["max_damage"],
                min_damage=weapon["min_damage"],
                damage_max_range=weapon["damage_max_range"],
                damage_min_range=weapon["damage_min_range"]
            )
            weapons.append(new_weapon)

    Weapon.objects.bulk_create(weapons)