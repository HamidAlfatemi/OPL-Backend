# Generated by Django 4.2.1 on 2023-05-25 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0005_alter_questions_title_alter_submittedquestions_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questions",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="submittedquestions",
            name="description",
            field=models.TextField(),
        ),
    ]
