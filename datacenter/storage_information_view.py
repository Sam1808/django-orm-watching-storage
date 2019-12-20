from datacenter.models import Visit, format_duration
from django.shortcuts import render


def storage_information_view(request):
    not_leaved_visit_journal = Visit.objects.filter(leaved_at=None)

    non_closed_visits= []

    for visit in not_leaved_visit_journal:
        duration = visit.get_duration()
        visit_description = {
            "who_entered": visit.passcard,
            "entered_at": visit.entered_at,
            "duration": format_duration(duration),
        }

        non_closed_visits.append(visit_description)

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
