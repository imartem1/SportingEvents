from django.shortcuts import render
from . import utils
from .models import Event, EventData, EventDetail, Person
from collections import defaultdict, OrderedDict


def index(request):
    # обновляем записи с главной
    utils.update_records()
    return render(request, 'index.html')


def start_list(request):
    # создаем словарь событий
    events = dict()
    # циклом проходим по событиям
    for event in Event.objects.all():
        # извлекаем данные по конкретному событию
        event_detail = EventDetail.objects.filter(event=event)
        # добавляем в словарь
        if event.name in events:
            events[event.name].append(event_detail)
        else:
            events[event.name] = [event_detail]

    # рендерим данные событий из словаря
    return render(request, 'start_list.html', {'events': events})


def start_protocol(request, id):

    # получаем данные по конректному мероприятию
    results = EventData.objects.filter(event_detail__id=id)
    return render(request, 'start_protocol.html', {'start_protocol_data': results})


def result_list(request):
    # создаем словарь событий
    events = dict()
    # циклом проходим по событиям
    for event in Event.objects.all():
        # извлекаем данные по конкретному событию
        event_detail = EventDetail.objects.filter(event=event)
        # добавляем в словарь
        if event.name in events:
            events[event.name].append(event_detail)
        else:
            events[event.name] = [event_detail]

    # рендерим данные событий из словаря
    return render(request, 'result_list.html', {'events': events})


def round_results(request, event_id, round_number):
    results = EventData.objects.filter(event_detail__event__id=event_id,
                                       event_detail__round_number=round_number).order_by("time")
    return render(request, 'round_result_protocol.html', {'results': results})


def result_protocol(request, event_id, round_number, heat_number):
    results = EventData.objects.filter(event_detail__event__id=event_id,
                                       event_detail__round_number=round_number,
                                       event_detail__heat_number=heat_number).order_by("time")

    return render(request, 'round_result_protocol.html', {'results': results})


def final_protocol_list(request):
    events = Event.objects.all()
    return render(request, 'final_protocol_list.html', {'events': events})


def final_protocol(request, event_id):

    results = defaultdict(dict)
    for result in EventData.objects.filter(event_detail__event__id=event_id).values("runner", 'event_detail').order_by(
            'runner', 'event_detail'):
        person = Person.objects.get(id=result['runner'])
        event_detail = EventDetail.objects.get(id=result['event_detail'])
        personal_data = EventData.objects.get(runner=person, event_detail=event_detail)
        results[event_detail.round_number][person] = personal_data.time

    sorted_results = list()
    for round_n in range(len(results), 0, -1):
        data = sorted(results[round_n].items(), key=lambda x: x[1])
        sorted_results.append(data)


    final_result = OrderedDict()

    for person, time in sorted_results[0]:
        final_result[person] = [time]
    for round_n in range(1, len(sorted_results)):
        for person, time in sorted_results[round_n]:
            if person in final_result:
                final_result[person].insert(0, time)
            else:
                final_result[person] = [time]

    return render(request, 'final_protocol.html', {'results': final_result})
