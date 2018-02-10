from django.db import models

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    """This class represents the bucketlist model."""
    phone = PhoneNumberField(blank=False, unique=True)
    discount = models.DecimalField(blank=True, default=1, decimal_places=2, max_digits=5)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.phone, self.discount)
