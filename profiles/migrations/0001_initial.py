# Generated by Django 4.2 on 2024-10-13 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkExperienceBullets",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bullet_point", models.CharField(max_length=150)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="work_bullets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Work Experience Bullets",
            },
        ),
        migrations.CreateModel(
            name="WorkExperience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                ("present", models.BooleanField(default=False)),
                ("position", models.CharField(max_length=150)),
                ("organization", models.CharField(max_length=150)),
                (
                    "bullet_points",
                    models.ManyToManyField(to="profiles.workexperiencebullets"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="work_experience",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Work Experience",
            },
        ),
        migrations.CreateModel(
            name="Summary",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("summary", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="summary_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Skills",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("skillset", models.TextField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_skills",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EducationBullets",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bullet_point", models.CharField(max_length=150)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="education_bullets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Education Bullets",
            },
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_year", models.CharField(max_length=4)),
                ("end_year", models.CharField(blank=True, max_length=4, null=True)),
                ("degree", models.CharField(max_length=150)),
                ("school_name", models.CharField(max_length=150)),
                ("grade", models.CharField(max_length=50)),
                (
                    "bullet_points",
                    models.ManyToManyField(to="profiles.educationbullets"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="education",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Education",
            },
        ),
        migrations.CreateModel(
            name="ContactInformation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(blank=True, max_length=100, null=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("address1", models.CharField(blank=True, max_length=100, null=True)),
                ("address2", models.CharField(blank=True, max_length=100, null=True)),
                ("city", models.CharField(blank=True, max_length=50, null=True)),
                ("zip_code", models.CharField(blank=True, max_length=10, null=True)),
                ("country", models.CharField(blank=True, max_length=50, null=True)),
                ("linkedin", models.URLField(blank=True, null=True)),
                ("github", models.URLField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact_information",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Contact Information",
            },
        ),
    ]
