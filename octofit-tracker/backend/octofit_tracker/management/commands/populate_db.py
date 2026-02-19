from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        
        # Delete existing data using Django ORM
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Existing data cleared'))
        
        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Assemble! Team of Marvel superheroes committed to fitness excellence'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League fitness warriors saving the world one workout at a time'
        )
        self.stdout.write(self.style.SUCCESS('Teams created'))
        
        # Create Users
        self.stdout.write('Creating users...')
        marvel_users = [
            User.objects.create(name='Tony Stark', email='ironman@marvel.com', team='Team Marvel'),
            User.objects.create(name='Steve Rogers', email='captain@marvel.com', team='Team Marvel'),
            User.objects.create(name='Natasha Romanoff', email='blackwidow@marvel.com', team='Team Marvel'),
            User.objects.create(name='Thor Odinson', email='thor@marvel.com', team='Team Marvel'),
            User.objects.create(name='Bruce Banner', email='hulk@marvel.com', team='Team Marvel'),
        ]
        
        dc_users = [
            User.objects.create(name='Clark Kent', email='superman@dc.com', team='Team DC'),
            User.objects.create(name='Bruce Wayne', email='batman@dc.com', team='Team DC'),
            User.objects.create(name='Diana Prince', email='wonderwoman@dc.com', team='Team DC'),
            User.objects.create(name='Barry Allen', email='flash@dc.com', team='Team DC'),
            User.objects.create(name='Arthur Curry', email='aquaman@dc.com', team='Team DC'),
        ]
        
        all_users = marvel_users + dc_users
        self.stdout.write(self.style.SUCCESS(f'Created {len(all_users)} users'))
        
        # Create Activities
        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Swimming', 'Cycling', 'Weight Training', 'Boxing', 'Yoga']
        activities_created = 0
        
        for user in all_users:
            # Create 5-10 activities per user
            for i in range(5, 11):
                activity_type = activity_types[i % len(activity_types)]
                duration = 30 + (i * 10)  # 30 to 130 minutes
                calories = duration * 8  # Approximate calories
                date = timezone.now() - timedelta(days=i)
                
                Activity.objects.create(
                    user_email=user.email,
                    activity_type=activity_type,
                    duration=duration,
                    calories_burned=calories,
                    date=date
                )
                activities_created += 1
        
        self.stdout.write(self.style.SUCCESS(f'Created {activities_created} activities'))
        
        # Create Leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        for user in all_users:
            user_activities = Activity.objects.filter(user_email=user.email)
            total_calories = sum(activity.calories_burned for activity in user_activities)
            total_activities = user_activities.count()
            
            Leaderboard.objects.create(
                user_email=user.email,
                team=user.team,
                total_calories=total_calories,
                total_activities=total_activities,
                rank=0  # Will be calculated based on total_calories
            )
        
        # Update ranks based on total_calories
        leaderboard_entries = Leaderboard.objects.all().order_by('-total_calories')
        for rank, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = rank
            entry.save()
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(all_users)} leaderboard entries'))
        
        # Create Workouts
        self.stdout.write('Creating workouts...')
        workouts = [
            {
                'name': 'Hulk Smash Circuit',
                'description': 'High-intensity strength training inspired by the Hulk. Includes heavy lifting, power movements, and explosive exercises.',
                'difficulty': 'Hard',
                'duration': 60,
                'calories_estimate': 600
            },
            {
                'name': 'Spider-Sense Agility Training',
                'description': 'Improve reflexes and agility with quick movements, ladder drills, and coordination exercises.',
                'difficulty': 'Medium',
                'duration': 45,
                'calories_estimate': 400
            },
            {
                'name': 'Captain America Endurance Run',
                'description': 'Long-distance running program to build stamina and cardiovascular endurance like a super soldier.',
                'difficulty': 'Medium',
                'duration': 50,
                'calories_estimate': 500
            },
            {
                'name': 'Black Widow Combat Conditioning',
                'description': 'Martial arts-inspired workout combining cardio, strength, and flexibility training.',
                'difficulty': 'Hard',
                'duration': 55,
                'calories_estimate': 550
            },
            {
                'name': 'Flash Speed Training',
                'description': 'Sprint intervals and speed work to maximize your velocity and quickness.',
                'difficulty': 'Hard',
                'duration': 40,
                'calories_estimate': 480
            },
            {
                'name': 'Wonder Woman Warrior Workout',
                'description': 'Full-body strength and power training with a focus on functional movements.',
                'difficulty': 'Medium',
                'duration': 50,
                'calories_estimate': 520
            },
            {
                'name': 'Aquaman Swimming Challenge',
                'description': 'Pool-based workout focusing on swimming technique, endurance, and water resistance training.',
                'difficulty': 'Medium',
                'duration': 45,
                'calories_estimate': 450
            },
            {
                'name': 'Iron Man Tech Recovery',
                'description': 'Low-impact recovery session with stretching, foam rolling, and mobility work.',
                'difficulty': 'Easy',
                'duration': 30,
                'calories_estimate': 150
            },
            {
                'name': 'Thor Hammer Strength',
                'description': 'Heavy compound lifting focusing on building raw power and strength.',
                'difficulty': 'Hard',
                'duration': 65,
                'calories_estimate': 580
            },
            {
                'name': 'Batman Dark Knight Core',
                'description': 'Core-focused workout targeting abs, back, and overall stability for crime-fighting readiness.',
                'difficulty': 'Medium',
                'duration': 35,
                'calories_estimate': 300
            },
        ]
        
        for workout_data in workouts:
            Workout.objects.create(**workout_data)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts)} workouts'))
        
        # Summary
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(f'Teams: {Team.objects.count()}')
        self.stdout.write(f'Users: {User.objects.count()}')
        self.stdout.write(f'Activities: {Activity.objects.count()}')
        self.stdout.write(f'Leaderboard Entries: {Leaderboard.objects.count()}')
        self.stdout.write(f'Workouts: {Workout.objects.count()}')
        self.stdout.write(self.style.SUCCESS('==================================='))
