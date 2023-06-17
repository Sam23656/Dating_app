from django.db import models


# Create your models here.

class Profile(models.Model):
    Name = models.CharField(max_length=50)
    Sure_Name = models.CharField(max_length=50)
    Age = models.PositiveIntegerField()

    STATUS = (
        ("st", "Учусь"),
        ("wk", "Работаю"),
        ("sd", "Туплю"),
        ("mm", "Мамкин миллиардер"),
        ("mp", "Мамин бродяга, папин симпотяга"),
    )

    Status = models.CharField(max_length=50, choices=STATUS)
    Salary = models.IntegerField()
    Description = models.TextField()

    def __str__(self):
        return f"{self.Name} - {self.Sure_Name}"

    def get_absolute_url(self):
        return f"/{self.pk}"
