# Generated by Django 4.2.1 on 2023-05-30 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "questions",
            "0019_submittedquestions_citation_submittedquestions_email_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="submittedquestions",
            name="species",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
