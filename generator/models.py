from django.db import models


class GeneratorModel(models.Model):
    field1 = models.TextField()
    field2 = models.TextField()

    # def __str__(self):
    #     return self.name
