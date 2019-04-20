from django.core.management import BaseCommand
from django.db import IntegrityError

from jobsboard.Skills import LANGUAGE, STATISTICS, CODING, DISCIPLINE, TECHNICAL, OTHER, prepop
from jobsboard.models import SkillTags


class Command(BaseCommand):
    # Show this when the user types help
    help = "populates db with tags"

    # A command must define handle()
    def handle(self, *args, **options):

        for discipline, _list in prepop.items():
            for item in _list:
                try:
                    SkillTags.objects.create(type=discipline, name=item)
                except IntegrityError:
                    pass

        self.stdout.write("done!")
