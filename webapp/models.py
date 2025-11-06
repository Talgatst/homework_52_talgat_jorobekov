from django.db import models


from django.db import models

status_choices = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано'),
]


class Task(models.Model):
    description = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Описание задачи"
    )
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default='new',
        verbose_name="Статус"
    )
    deadline_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата выполнения"
    )

    def __str__(self):
        return self.description
