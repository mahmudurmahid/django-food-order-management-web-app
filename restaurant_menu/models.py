from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starters", "Starters"),
    ("appetizers", "Appetizers"),
    ("main_courses", "Main Courses"),
    ("desserts", "Desserts")
)

FOOD_AVAILABILITY = (
    (0, "Unavailable"),
    (1, "Available"),
)

# Create your models here.
class FoodItem(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    food_availability = models.IntegerField(choices=FOOD_AVAILABILITY, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    # returns the string representation of the model (i.e. the meal name)
    def __str__(self):
        return self.meal
