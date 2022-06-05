from django.shortcuts import render
from weapons.db_script import push_all_weapons
from weapons.models import Weapon


def index(request):
    if not Weapon.objects.exists():
        push_all_weapons(push_db=True)
    return render(request, 'index.html')