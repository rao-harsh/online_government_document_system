# Generated by Django 4.1.7 on 2023-03-04 18:12

import application.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Income",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("Applicant_Name", models.CharField(max_length=50)),
                ("Applicant_Address", models.CharField(max_length=50)),
                ("Native_Address", models.CharField(max_length=50)),
                ("Occupation_Details", models.CharField(max_length=50)),
                ("Total_Family_Members", models.CharField(max_length=50)),
                ("Family_Annual_Income", models.CharField(max_length=50)),
                ("No_Of_Family_Members_Earning", models.CharField(max_length=50)),
                ("Annual_Average_Electricity_Bill", models.CharField(max_length=50)),
                ("Family_Member1_Name", models.CharField(max_length=50)),
                ("Relation_With_Applicant1", models.CharField(max_length=50)),
                ("Age_1", models.CharField(max_length=50)),
                ("Occupation_1", models.CharField(max_length=50)),
                ("Annual_Income_1", models.CharField(max_length=50)),
                ("Family_Member2_Name", models.CharField(max_length=50)),
                ("Relation_With_Applicant2", models.CharField(max_length=50)),
                ("Age_2", models.CharField(max_length=50)),
                ("Occupation_2", models.CharField(max_length=50)),
                ("Annual_Income_2", models.CharField(max_length=10)),
                ("Aadhar_Card_Number", models.CharField(max_length=50)),
                (
                    "Aadhar_Card_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
                ("Ration_Card_Number", models.CharField(max_length=50)),
                (
                    "Ration_Card_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
                ("Electricity_Bill_Number", models.CharField(max_length=50)),
                (
                    "Electricity_Bill_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
                ("Election_Card_Number", models.CharField(max_length=50)),
                (
                    "Election_Card_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
                ("Witness1_Full_Name", models.CharField(max_length=50)),
                ("Witness1_Age", models.CharField(max_length=50)),
                ("Witness1_Occupation_Details", models.CharField(max_length=50)),
                ("Witness1_Permanent_Address", models.CharField(max_length=50)),
                ("Witness1_Aadhar_Card_Number", models.CharField(max_length=50)),
                (
                    "Witness1_Aadhar_Card_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
                (
                    "Witness1_Signature_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
                ("Witness2_Full_Name", models.CharField(max_length=50)),
                ("Witness2_Age", models.CharField(max_length=50)),
                ("Witness2_Occupation_Details", models.CharField(max_length=50)),
                ("Witness2_Permanent_Address", models.CharField(max_length=50)),
                ("Witness2_Aadhar_Card_Number", models.CharField(max_length=50)),
                (
                    "Witness2_Aadhar_Card_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
                (
                    "Witness2_Signature_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
                (
                    "Applicant_Signature_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
                (
                    "Applicant_Passport_Size_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
                ("Date_Of_Application", models.CharField(max_length=50)),
                (
                    "Self_Declaration_Certificate_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Non_Creamy_Layer",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("Applicant_Name", models.CharField(max_length=50)),
                ("Date_Of_Birth", models.CharField(max_length=50)),
                ("Permanent_Address", models.CharField(max_length=50)),
                ("Contact_Number", models.CharField(max_length=50)),
                ("Cast_OR_Sub_Cast", models.CharField(max_length=50)),
                ("Occupation_Details", models.CharField(max_length=50)),
                ("Father_Name", models.CharField(max_length=50)),
                ("Mother_Name", models.CharField(max_length=50)),
                ("Spouse_Name", models.CharField(blank=True, max_length=50, null=True)),
                ("Father_Occupation_Details", models.CharField(max_length=50)),
                ("Ration_Card_Number", models.CharField(max_length=50)),
                ("Electricity_Bill_Number", models.CharField(max_length=50)),
                (
                    "Electricity_Bill_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
                (
                    "SEBC_Cast_Certificate_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
                (
                    "Income_Certificate_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
                ("Witness1_Full_Name", models.CharField(max_length=50)),
                ("Witness1_Age", models.CharField(max_length=50)),
                ("Witness1_Occupation_Details", models.CharField(max_length=10)),
                ("Witness1_Permanent_Address", models.CharField(max_length=50)),
                ("Witness1_Aadhar_Card_Number", models.CharField(max_length=50)),
                (
                    "Witness1_Aadhar_Card_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
                (
                    "Witness1_Signature_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
                ("Witness2_Full_Name", models.CharField(max_length=50)),
                ("Witness2_Age", models.CharField(max_length=50)),
                ("Witness2_Occupation_Details", models.CharField(max_length=50)),
                ("Witness2_Permanent_Address", models.CharField(max_length=50)),
                ("Witness2_Aadhar_Card_Number", models.CharField(max_length=50)),
                (
                    "Witness2_Aadhar_Card_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
                (
                    "Witness2_Signature_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
                (
                    "Applicant_Passport_Size_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
                (
                    "Applicant_Signature_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
                ("Date_Of_Application", models.CharField(max_length=50)),
                (
                    "Self_Declaration_Image",
                    models.ImageField(upload_to=application.models.get_upload_path),
                ),
            ],
        ),
        migrations.AddField(
            model_name="customuser",
            name="contact",
            field=models.CharField(default=8849978758, max_length=10),
            preserve_default=False,
        ),
    ]
