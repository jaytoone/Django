from django.db import models
from adaptor.model import CsvModel

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField
class Profile(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=150,unique=True)
    profile = models.TextField()
    def __str__(self):
        return self.name


class mycsvmodel(CsvModel):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=150,unique=True)
    profile = models.TextField()

    class Meta:
        delimiter = ','

if __name__=='__main__':
    my_csv_list = mycsvmodel.import_data(data=open('test.csv'))
    first_line = my_csv_list[0]
    first_line.age
