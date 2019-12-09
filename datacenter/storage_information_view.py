from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    not_leaved_visitor_list = Visit.objects.filter(leaved_at=None)

    non_closed_visits= []

    for visitor in not_leaved_visitor_list:
        total_time = Visit.get_duration(visitor)
        visit_description = {
            "who_entered": visitor.passcard,
            "entered_at": visitor.entered_at,
            "duration": Visit.format_duration(total_time),
        }

        non_closed_visits.append(visit_description)

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
