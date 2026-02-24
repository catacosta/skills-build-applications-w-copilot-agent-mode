from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes team')
        dc = Team.objects.create(name='DC', description='DC superheroes team')

        # Users
        users = [
            User(email='tony@marvel.com', name='Tony Stark', team=marvel.name),
            User(email='steve@marvel.com', name='Steve Rogers', team=marvel.name),
            User(email='bruce@marvel.com', name='Bruce Banner', team=marvel.name),
            User(email='clark@dc.com', name='Clark Kent', team=dc.name),
            User(email='bruce@dc.com', name='Bruce Wayne', team=dc.name),
            User(email='diana@dc.com', name='Diana Prince', team=dc.name),
        ]
        User.objects.bulk_create(users)

        # Activities
        Activity.objects.bulk_create([
            Activity(user='Tony Stark', activity_type='Running', duration=30, date=timezone.now()),
            Activity(user='Steve Rogers', activity_type='Cycling', duration=45, date=timezone.now()),
            Activity(user='Clark Kent', activity_type='Swimming', duration=60, date=timezone.now()),
        ])

        # Leaderboard
        Leaderboard.objects.bulk_create([
            Leaderboard(team=marvel.name, points=120),
            Leaderboard(team=dc.name, points=110),
        ])

        # Workouts
        Workout.objects.bulk_create([
            Workout(name='Super Strength', description='Strength workout for heroes', difficulty='Hard'),
            Workout(name='Speed Run', description='Speed and agility training', difficulty='Medium'),
        ])

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
