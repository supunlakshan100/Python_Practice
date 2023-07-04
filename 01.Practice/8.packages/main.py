from backend.models import Person
from frontend.validators import is_valid_age

# age = "40"
age = 30
print(is_valid_age(age))

p = Person("Supun")
print(p)
