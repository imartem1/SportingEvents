from pathlib import Path
from django.conf import settings
import pandas as pd
from .models import EventData, EventDetail, Event, Person


def path_competition_data():
    base_dir = Path(settings.BASE_DIR)
    return base_dir / 'competition_data'


def get_paths_of_files(files_extension='lif'):
    data_path = path_competition_data()
    paths = list(data_path.glob(f'*.{files_extension}'))
    return paths


def convert_to_df(file_name):
    # конвертируем данные lif в data frame pandas
    base_settings = {'sep': ',', 'encoding': 'utf-16'}
    df = pd.read_csv(file_name, **base_settings, skiprows=[0])
    df = df.iloc[:, 0:7]
    df.columns = ['number', 'edu_number', '_id', 'last_name', 'first_name', 'edu_name', 'time']
    index = 0
    df['time'] = df['time'].astype(str)
    for time in df['time']:
        if time != "nan" and ':' not in time:
            df.at[index, 'time'] = f'0:{time}'
        index += 1
    df.loc[df.time == 'nan', 'time'] = "Нет данных"
    df_tags = pd.read_csv(file_name, **base_settings, nrows=0, index_col=0).iloc[:, 0:4].columns.to_list()
    return {'df': df, 'tags': df_tags}


def update_records():
    #  обновляем данные БД
    paths = get_paths_of_files()
    Person.objects.all().delete()
    Event.objects.all().delete()
    EventDetail.objects.all().delete()
    EventData.objects.all().delete()

    if len(paths) > 0:
        for file in paths:
            data = convert_to_df(file)
            tags = data['tags']
            try:
                event = Event.objects.get(name=tags[3])
            except Event.DoesNotExist:
                event = Event(name=tags[3])
                event.save()

            event_detail = EventDetail(event_number=int(float(tags[0])),
                                       round_number=int(float(tags[1])),
                                       heat_number=int(float(tags[2])),
                                       event=event)
            event_detail.save()

            event_data = data['df'].to_dict('records')

            model_instances = list()
            for record in event_data:

                last_name = record['last_name']
                first_name = record['first_name']
                try:
                    person = Person.objects.get(first_name=first_name, last_name=last_name)
                    print(person)
                except Person.DoesNotExist:
                    person = Person(first_name=first_name, last_name=last_name)
                    person.save()

                model_instances.append(
                    EventData(
                        event_detail=event_detail,
                        person_id=record['_id'],
                        number=record['number'],
                        edu_number=record['edu_number'],
                        edu_name=record['edu_name'],
                        runner=person,
                        time=record['time'],
                    )
                )

            EventData.objects.bulk_create(model_instances)
