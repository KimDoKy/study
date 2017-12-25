import json
from functools import wraps
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def bot(view_fn):
    @wraps(view_fn)
    @csrf_exempt
    def wrap(request, *args, **kwargs):
        if request.method == 'POST':
            request.JSON = json.loads(request.body.decode('utf8'))
        else:
            request.JSON = {}
        return JsonResponse(view_fn(request, *args, **kwargs) or {})
    return wrap
