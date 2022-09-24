from django.db import models


class Calculator(models.Model):
    name = models.CharField(max_length=5)

    class Meta:
        db_table = 'Floating Point Calculator'
        verbose_name_plural = "Floating Point Calculator"
    def __str__(self):
        return '%s-%s' % (self.name)