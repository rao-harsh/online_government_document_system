from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import random
# Create your models here.


def generate_unique_id(model, field_name):
    while True:
        id = random.randint(10000, 99999)
        if not model.objects.filter(**{field_name: id}).exists():
            return id


def get_upload_path(instance, filename):
    return f"images/{instance.Applicant_Name}/{filename}"


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email and password:
            raise ValueError("The Email and Password must be provided")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name


class Income(models.Model):
    id = models.BigAutoField(primary_key=True)
    Applicant_Name = models.CharField(
        max_length=50,    null=False, blank=False)
    Applicant_Address = models.CharField(
        max_length=50,    null=False, blank=False)
    Native_Address = models.CharField(
        max_length=50,    null=False, blank=False)
    Occupation_Details = models.CharField(
        max_length=50,    null=False, blank=False)
    Total_Family_Members = models.CharField(
        max_length=50,    null=False, blank=False)
    Family_Annual_Income = models.CharField(
        max_length=50,    null=False, blank=False)
    No_Of_Family_Members_Earning = models.CharField(
        max_length=50,    null=False, blank=False)
    Annual_Average_Electricity_Bill = models.CharField(
        max_length=50,    null=False, blank=False)
    Family_Member1_Name = models.CharField(
        max_length=50,    null=False, blank=False)
    Relation_With_Applicant1 = models.CharField(
        max_length=50,    null=False, blank=False)
    Age_1 = models.CharField(max_length=50,    null=False, blank=False)
    Occupation_1 = models.CharField(max_length=50,    null=False, blank=False)
    Annual_Income_1 = models.CharField(
        max_length=50,    null=False, blank=False)
    Family_Member2_Name = models.CharField(
        max_length=50,    null=False, blank=False)
    Relation_With_Applicant2 = models.CharField(
        max_length=50,    null=False, blank=False)
    Age_2 = models.CharField(max_length=50,    null=False, blank=False)
    Occupation_2 = models.CharField(max_length=50,    null=False, blank=False)
    Annual_Income_2 = models.CharField(
        max_length=10,    null=False, blank=False)
    Aadhar_Card_Number = models.CharField(
        max_length=50,    null=False, blank=False)
    Aadhar_Card_Image = models.ImageField(upload_to=get_upload_path)
    Ration_Card_Number = models.CharField(
        max_length=50,    null=False, blank=False)
    Ration_Card_Image = models.ImageField(upload_to=get_upload_path)
    Electricity_Bill_Number = models.CharField(
        max_length=50,    null=False, blank=False)
    Electricity_Bill_Image = models.ImageField(upload_to=get_upload_path)
    Election_Card_Number = models.CharField(
        max_length=50,    null=False, blank=False)
    Election_Card_Image = models.ImageField(upload_to=get_upload_path)
    Witness1_Full_Name = models.CharField(
        max_length=50,    null=False, blank=False)
    Witness1_Age = models.CharField(max_length=50,    null=False, blank=False)
    Witness1_Occupation_Details = models.CharField(
        max_length=50,    null=False, blank=False)
    Witness1_Permanent_Address = models.CharField(
        max_length=50,    null=False, blank=False)
    Witness1_Aadhar_Card_Number = models.CharField(
        max_length=50,    null=False, blank=False)
    Witness1_Aadhar_Card_Image = models.ImageField(upload_to=get_upload_path)
    Witness1_Signature_Image = models.ImageField(upload_to=get_upload_path)
    Witness2_Full_Name = models.CharField(
        max_length=50,    null=False, blank=False)
    Witness2_Age = models.CharField(max_length=50,    null=False, blank=False)
    Witness2_Occupation_Details = models.CharField(
        max_length=50,    null=False, blank=False)
    Witness2_Permanent_Address = models.CharField(
        max_length=50,    null=False, blank=False)
    Witness2_Aadhar_Card_Number = models.CharField(
        max_length=50,    null=False, blank=False)
    Witness2_Aadhar_Card_Image = models.ImageField(upload_to=get_upload_path)
    Witness2_Signature_Image = models.ImageField(upload_to=get_upload_path)
    Applicant_Signature_Image = models.ImageField(upload_to=get_upload_path)
    Applicant_Passport_Size_Image = models.ImageField(
        upload_to=get_upload_path)
    Date_Of_Application = models.CharField(
        max_length=50,    null=False, blank=False)
    Self_Declaration_Certificate_Image = models.ImageField(
        upload_to=get_upload_path)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id}-{self.Applicant_Name}"

    def save(self):
        self.id = generate_unique_id(Income, "id")
        super(Income, self).save()


class Non_Creamy_Layer(models.Model):
    id = models.BigAutoField(primary_key=True)
    Applicant_Name = models.CharField(max_length=50,   null=False, blank=False)
    Date_Of_Birth = models.CharField(max_length=50,   null=False, blank=False)
    Permanent_Address = models.CharField(
        max_length=50,   null=False, blank=False)
    Contact_Number = models.CharField(max_length=50,   null=False, blank=False)
    Cast_OR_Sub_Cast = models.CharField(
        max_length=50,   null=False, blank=False)
    Occupation_Details = models.CharField(
        max_length=50,   null=False, blank=False)
    Father_Name = models.CharField(max_length=50,   null=False, blank=False)
    Mother_Name = models.CharField(max_length=50,   null=False, blank=False)
    Spouse_Name = models.CharField(max_length=50,   null=True, blank=True)
    Father_Occupation_Details = models.CharField(
        max_length=50,   null=False, blank=False)
    Ration_Card_Number = models.CharField(
        max_length=50,   null=False, blank=False)
    Electricity_Bill_Number = models.CharField(
        max_length=50,   null=False, blank=False)
    Electricity_Bill_Image = models.ImageField(upload_to=get_upload_path)
    SEBC_Cast_Certificate_Image = models.ImageField(upload_to=get_upload_path)
    Income_Certificate_Image = models.ImageField(upload_to=get_upload_path)
    Witness1_Full_Name = models.CharField(
        max_length=50,   null=False, blank=False)
    Witness1_Age = models.CharField(max_length=50,   null=False, blank=False)
    Witness1_Occupation_Details = models.CharField(
        max_length=10,   null=False, blank=False)
    Witness1_Permanent_Address = models.CharField(
        max_length=50,   null=False, blank=False)
    Witness1_Aadhar_Card_Number = models.CharField(
        max_length=50,   null=False, blank=False)
    Witness1_Aadhar_Card_Image = models.ImageField(upload_to=get_upload_path)
    Witness1_Signature_Image = models.ImageField(upload_to=get_upload_path)
    Witness2_Full_Name = models.CharField(
        max_length=50,   null=False, blank=False)
    Witness2_Age = models.CharField(max_length=50,   null=False, blank=False)
    Witness2_Occupation_Details = models.CharField(
        max_length=50,   null=False, blank=False)
    Witness2_Permanent_Address = models.CharField(
        max_length=50,   null=False, blank=False)
    Witness2_Aadhar_Card_Number = models.CharField(
        max_length=50,   null=False, blank=False)
    Witness2_Aadhar_Card_Image = models.ImageField(upload_to=get_upload_path)
    Witness2_Signature_Image = models.ImageField(upload_to=get_upload_path)
    Applicant_Passport_Size_Image = models.ImageField(
        upload_to=get_upload_path)
    Applicant_Signature_Image = models.ImageField(upload_to=get_upload_path)
    Date_Of_Application = models.CharField(
        max_length=50,   null=False, blank=False)
    Self_Declaration_Image = models.ImageField(upload_to=get_upload_path)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id}-{self.Applicant_Name}"

    def save(self):
        self.id = generate_unique_id(Non_Creamy_Layer, "id")
        super(Non_Creamy_Layer, self).save()
