from django.shortcuts import render
from weapons.db_script import push_all_weapons
from weapons.models import Weapon


def index(request):
    return render(request, 'index.html')