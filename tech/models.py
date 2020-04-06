from django.db import models



class Comp(models.Model):
    name = models.CharField(max_length=100)
    date_ins = models.CharField(max_length=100)
    number = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    place = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    conf = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    msoffice = models.CharField(max_length=100)
    buh = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    inwork = models.CharField(max_length=100)
    decommissioned = models.CharField(max_length=100)
    biosuser = models.CharField(max_length=100)
    biossupper = models.CharField(max_length=100)

    # author = models.ForeignKey(Author, blank=True, null=True)
    # author_email = models.EmailField('Author email', max_length=75, blank=True)
    # imported = models.BooleanField(default=False)
    # published = models.DateField('Published', blank=True, null=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # categories = models.ManyToManyField(Category, blank=True)

    # def __str__(self):
    #     return self.name

# Create your models here.
