from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode = passcode)
    # Программируем здесь
    all_visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in all_visits:
        visit_description = {}
        visit_description.update({"entered_at": visit.entered_at})
        visit_duration = Visit.get_duration(visit)
        visit_description.update({"duration": Visit.format_duration(visit_duration)})
        visit_description.update({"is_strange": Visit.is_visit_long(visit)})

        this_passcard_visits.append(visit_description)



    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
