from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode = passcode)
    all_visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in all_visits:
        visit_duration = Visit.get_duration(visit)
        visit_description = {
            "entered_at": visit.entered_at,
            "duration": Visit.format_duration(visit_duration),
            "is_strange": Visit.is_visit_long(visit),
        }

        this_passcard_visits.append(visit_description)

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
