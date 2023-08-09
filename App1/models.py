from django.db import models

# Create your models here.
class Employee:
    def __init__(self, Name, Age, BirthDay, email, Salary):
        self.Name = Name
        self.Age = Age
        self.BirthDay = BirthDay
        self.email = email
        self.Salary = Salary