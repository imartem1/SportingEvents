from django.db import models


class Event(models.Model):
    name = models.CharField(verbose_name="Название события", max_length=64, default='Event')

    def __str__(self):
        return f'{self.name}'


class EventDetail(models.Model):
    event_number = models.IntegerField(verbose_name='Номер события', null=True)
    round_number = models.IntegerField(verbose_name='Номер круга', null=True)
    heat_number = models.IntegerField(verbose_name='Номер забега', null=True)

    event = models.ForeignKey(Event, verbose_name="Событие", on_delete=models.CASCADE, default="Event", null=True)

    def __str__(self):
        return f'{self.event}' \
               f'/{self.event_number}' \
               f'/{self.round_number}' \
               f'/{self.heat_number}'


class Person(models.Model):
    last_name = models.CharField(verbose_name="Фамилия участника", max_length=128, null=True)
    first_name = models.CharField(verbose_name="Имя участника", max_length=128, null=True)

    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class EventData(models.Model):
    event_detail = models.ForeignKey(EventDetail, verbose_name="Событие", on_delete=models.CASCADE, null=True)

    number = models.CharField(verbose_name="Место", max_length=8, null=True)
    person_id = models.CharField(verbose_name="Номер участника", max_length=8, null=True)
    edu_number = models.CharField(verbose_name="Номер образовательного учереждения", max_length=8, null=True)
    edu_name = models.CharField(verbose_name="Название образовательного учереждения", max_length=128, null=True)

    runner = models.ForeignKey(Person, verbose_name='Участник', on_delete=models.CASCADE, null=True)
    time = models.CharField(verbose_name="Время", max_length=8, null=True)

    def __str__(self):
        return f'{self.event_detail}' \
               f'/{self.runner.last_name} ' \
               f'{self.runner.first_name}' \


    def get_head_result(self):
        return {self.event_detail.heat_number: self.time}
