from django.http import HttpResponse
from .db_script import push_all_weapons

def populate(request):
    push_all_weapons(push_db=True)
    return HttpResponse("DB updated!")