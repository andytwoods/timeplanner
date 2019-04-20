import random

from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
from django.core.management import BaseCommand, call_command
import factory
from factory.fuzzy import FuzzyInteger

from timeplanner.task.factories import TaskFactory
from timeplanner.task.models import Task
from timeplanner.users.models import User


class Command(BaseCommand):

    # Show this when the user types help
    help = "populates db with fake data"

    # A command must define handle()
    def handle(self, *args, **options):

        site = Site.objects.first()
        if site.domain != 'localhost:8000':
            site.domain = 'www.spyrelabs.org'
            site.name = 'www.spyrelabs.org'
            site.save()

        try:
            SocialApp.objects.get(name='Paypal Application')
        except SocialApp.DoesNotExist:
            paypal_app = SocialApp(provider='paypal',
                                   name='Paypal Application',
                                   client_id='AX0UovJTfneT-r-vR7eIv8o-jvin6Dw3RwM_5qWtKLJcJO443yH3c-QqJ_JLaBgAfWkN-zKzcCVQREGJ',
                                   secret='ECpTS7SBU9oxRcwTYZLuxRikSXB9Usaw9Lguy_G8Mm1gaS70no6He83JkQ7D7JYzysxVi3pxY54H0nqF',)
            paypal_app.save()
            paypal_app.sites.add(site)
            paypal_app.save()

        admin = User.objects.filter(username='Andy').first()
        if admin is None:
            call_command('createsuperuser2', email='andytwoods@gmail.com', username="Andy", password='banana123' )
            admin = User.objects.filter(username='Andy').first()

        task = self.create_task()
        self.root = Task.add_root(instance=task)
        tasks = [task]
        for _ in range(10):
            task = self.create_task()
            parent:Task = random.choice(tasks)
            parent.add_child(instance=task)
            tasks.append(task)

    def create_task(self):
        task = Task(
            info=factory.Faker('text'),
            priority=random.randint(1, 3)
        )
        return task

