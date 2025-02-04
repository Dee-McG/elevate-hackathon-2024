# Generated by Django 4.2 on 2024-10-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0012_alter_education_grade"),
    ]

    operations = [
        migrations.AlterField(
            model_name="education",
            name="applied_skills",
            field=models.ManyToManyField(related_name="education", to="profiles.skill"),
        ),
        migrations.AlterField(
            model_name="education",
            name="bullet_points",
            field=models.ManyToManyField(
                related_name="related_experience", to="profiles.educationbullets"
            ),
        ),
        migrations.AlterField(
            model_name="workexperience",
            name="applied_skills",
            field=models.ManyToManyField(related_name="work", to="profiles.skill"),
        ),
        migrations.AlterField(
            model_name="workexperience",
            name="bullet_points",
            field=models.ManyToManyField(
                related_name="related_experience", to="profiles.workexperiencebullets"
            ),
        ),
    ]
