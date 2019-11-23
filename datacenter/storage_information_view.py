from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    # Программируем здесь

    not_leaved_visitor_list = Visit.objects.filter(leaved_at=None)

    non_closed_visits= []

    for visitor in not_leaved_visitor_list:
        visit_description = {}
        visit_description.update({"who_entered": visitor.passcard})
        visit_description.update({"entered_at": visitor.entered_at})
        total_time = Visit.get_duration(visitor)
        visit_description.update({"duration": Visit.format_duration(total_time)})
        non_closed_visits.append(visit_description)

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
