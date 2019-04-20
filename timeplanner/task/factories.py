import random

import factory
from factory.fuzzy import BaseFuzzyAttribute, FuzzyInteger

from timeplanner.task.models import Task


class FloatDP(BaseFuzzyAttribute):
    def fuzz(self):
        return round(random.uniform(0, 1), 2)


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    info = factory.Faker('text')
    priority = FuzzyInteger(1, 3)

