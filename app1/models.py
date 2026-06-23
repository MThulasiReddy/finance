from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Loan(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    borrower_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    loan_date = models.DateField()
    duration_months = models.IntegerField()
