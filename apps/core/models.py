from uuid import uuid4

from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.


class UUIDModel(TimeStampedModel):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)
