from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from .db_script import push_all_weapons
from .models import Weapon
from django.forms.models import model_to_dict

def populate(request):
    push_all_weapons(push_db=True)
    return HttpResponse("DB updated!")

def weapon_search(request):
    weapon_list = request.GET.get('weapon')
    weapon_obj = request.GET.get('object')
    payload = list()

    if weapon_list:
        query_result = Weapon.objects.filter(name__icontains=weapon_list)

        for weapon_result in query_result:
            payload.append(weapon_result.name)
        return JsonResponse({'status':200, 'data' : payload})
    elif weapon_obj:
        query_result = Weapon.objects.filter(name__icontains=weapon_obj)

        for weapon_result in query_result:
            payload.append(model_to_dict(weapon_result))
        return JsonResponse({'status':200, 'data' : payload})
    else:
        return HttpResponseBadRequest()