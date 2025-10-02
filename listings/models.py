from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Listing(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	location = models.CharField(max_length=255)
	host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class Booking(models.Model):
	listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
	guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
	check_in = models.DateField()
	check_out = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.guest} booking for {self.listing}"

class Review(models.Model):
	listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
	rating = models.PositiveSmallIntegerField()
	comment = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Review by {self.user} for {self.listing}"
