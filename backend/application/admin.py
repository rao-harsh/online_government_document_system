from django.contrib import admin
from . import models
# Register your models here.
admin.site.register([models.CustomUser,models.Income,models.Non_Creamy_Layer])