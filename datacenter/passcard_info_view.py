from datacenter.models import Passcard
from datacenter.models import Visit,format_duration
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode = passcode)
    all_visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in all_visits:
        duration = visit.get_duration()
        visit_description = {
            "entered_at": visit.entered_at,
            "duration": format_duration(duration),
            "is_strange": visit.is_visit_long(),
        }

        this_passcard_visits.append(visit_description)

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
