from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.utils import timezone

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Data(models.Model):
    """This class represents the bucketlist model."""
    loader = models.BooleanField(blank=False)
    cutter = models.BooleanField(blank=False)
    calculatedInPlace = models.BooleanField(blank=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.loader, self.cutter, self.calculatedInPlace)


class Customer(models.Model):
    """This class represents the bucketlist model."""
    phone = PhoneNumberField(blank=False, unique=False)
    discount = models.DecimalField(blank=True, default=1, decimal_places=2, max_digits=5)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.phone, self.discount)


class Locality(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(blank=False, unique=True, max_length=25)
    distanceBelogorsk = models.IntegerField(blank=False, default=0)
    distanceSkovorodino = models.IntegerField(blank=False, default=0)
    distanceTygda = models.IntegerField(blank=False, default=0)
    data = models.ForeignKey(Data, related_name='localitys', on_delete=models.CASCADE, default=1)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name, self.distanceBelogorsk, self.distanceSkovorodino, self.distanceTygda)


class Scrapyard(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(blank=False, unique=True, max_length=25)
    price = models.DecimalField(blank=False, default=1, decimal_places=2, max_digits=10)
    coef = models.DecimalField(blank=False, default=1, decimal_places=2, max_digits=5)
    data = models.ForeignKey(Data, related_name='scrapyards', on_delete=models.CASCADE, null=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name, self.price)


class Transport(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(blank=False, max_length=25)
    price = models.DecimalField(blank=False, default=1, decimal_places=2, max_digits=10)
    tonn = models.DecimalField(blank=False, default=1, decimal_places=2, max_digits=10)
    data = models.ForeignKey(Data, related_name='transports', on_delete=models.CASCADE, null=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name, self.price, self.tonn)


class Email(models.Model):
    """This class represents the bucketlist model."""
    email = models.EmailField(blank=False, unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.email)


class Request(models.Model):
    phone = models.CharField(blank=False, max_length=15)
    loader = models.BooleanField(blank=False)
    cutter = models.BooleanField(blank=False)
    calculatedInPlace = models.BooleanField(blank=False)
    discount = models.CharField(blank=True, max_length=12)
    locality = models.CharField(blank=False, max_length=25)
    address = models.CharField(blank=True,max_length=125)
    scrapyard = models.CharField(blank=False, max_length=25)
    distantce = models.CharField(blank=False, max_length=10)
    transport = models.CharField(blank=False, max_length=25)
    cost = models.CharField(blank=False, max_length=12)
    tonn = models.CharField(blank=True, max_length=12)
    data = models.CharField(blank=True, max_length=25)
    comment = models.CharField(blank=True, max_length=400)
    createdDate = models.CharField(blank=False, max_length=50, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.createdDate = timezone.now()
        return super(Request, self).save(*args, **kwargs)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "Номер телефона: {}. Доплата по статусу: {}. \n" \
               "Наседенный пункт: {}. Адрес: {}.\n"\
            "Пункт приема: {}. Растояние {}.\n"\
            "Транспорт: {}. Вес: {}\n"\
            "Стоимость доставки: {}\n"\
            "Дата: {}.\n"\
            "Комментарий: {}\n"\
            "Грузщики: {}. Резчики: {}. Рассчет на месте: {}\n"\
            "Дата создания запроса {}".format(self.phone, self.discount, self.locality, self.address, self.scrapyard, self.distantce,
                           self.transport, self.tonn, self.cost, self.data, self.comment, self.loader, self.cutter,
                           self.calculatedInPlace, self.createdDate.__str__())
