from django.http import HttpResponse, JsonResponse
from .models import Weapon
from django.forms.models import model_to_dict
from .db_script import push_all_weapons

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
        try:
            query_result = Weapon.objects.get(name=weapon_obj)
        except Weapon.DoesNotExist:
            return JsonResponse({'status':404, 'data' : 'Weapon not found'})
        return JsonResponse({'status':200, 'data' : model_to_dict(query_result)})
    else:
        return JsonResponse({'status':404, 'data' : 'Weapon not found'})

def push_db(request):
    if not Weapon.objects.exists():
        push_all_weapons(push_db=True)
    return HttpResponse('')