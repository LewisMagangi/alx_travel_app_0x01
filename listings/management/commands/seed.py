from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing
import random

User = get_user_model()

SAMPLE_LISTINGS = [
    {
        "title": "Cozy Apartment in City Center",
        "description": "A lovely apartment close to all amenities.",
        "price": 120.00,
        "location": "Nairobi, Kenya"
    },
    {
        "title": "Beachside Bungalow",
        "description": "Enjoy the ocean breeze in this beautiful bungalow.",
        "price": 200.00,
        "location": "Mombasa, Kenya"
    },
    {
        "title": "Mountain Retreat",
        "description": "A peaceful retreat in the mountains.",
        "price": 150.00,
        "location": "Mt. Kenya, Kenya"
    },
]

class Command(BaseCommand):
    help = 'Seed the database with sample listings.'

    def handle(self, *args, **kwargs):
        # Get or create a default user to be the host
        user, _ = User.objects.get_or_create(username='host', defaults={'password': 'hostpass'})
        for data in SAMPLE_LISTINGS:
            listing, created = Listing.objects.get_or_create(
                title=data["title"],
                defaults={
                    "description": data["description"],
                    "price": data["price"],
                    "location": data["location"],
                    "host": user
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created listing: {listing.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Listing already exists: {listing.title}'))
        self.stdout.write(self.style.SUCCESS('Database seeding complete.'))
