from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    use_from = models.DateTimeField()
    use_to = models.DateTimeField()
    amount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], help_text='%값으로 입력하시오.')
    active = models.BooleanField()

    def __str__(self):
        return self.code
