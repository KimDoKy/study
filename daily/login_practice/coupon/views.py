import datetime
from django.shortcuts import render
from .models import Coupon


def reset_db(qs):
    for q in qs:
        q.use_1 = bool(False)
        q.use_2 = bool(False)
        q.save()


def coupon_list(request):
    qs = Coupon.objects.all()
    if request.method == 'POST':
        reset_bt = request.POST.get('reset')
        if reset_bt:
            reset_db(qs)
        use_1 = request.POST.get('use_1')
        use_2 = request.POST.get('use_2')
        if use_1:
            id, value = use_1.split(',')
            obj = qs.get(pk=int(id))
            if value == 'False' and obj.use_1 == bool(False):
                obj.use_1 = bool(True)
                obj.use_date = obj.use_date.now()
                obj.save()
        elif use_2:
            id, value = use_2.split(',')
            obj = qs.get(pk=int(id))
            if value == 'False' and obj.use_1 == bool(True):
                obj.use_2 = bool(True)
                obj.use_2_date = obj.use_2_date.now()
                obj.save()
    return render(request, 'coupon/coupon_list.html', {'lists':qs})
