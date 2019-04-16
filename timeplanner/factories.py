import factory
from factory.fuzzy import FuzzyInteger, FuzzyText, BaseFuzzyAttribute

from timeplanner.task.models import Task


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task



    cover_letter = factory.Faker('text')
    consultant = factory.SubFactory(ConsultantFactory)
