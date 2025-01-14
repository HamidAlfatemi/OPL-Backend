# Generated by Django 4.2.1 on 2023-05-26 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0009_rename_child_question_id_relatedquestions_child_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="relatedquestions",
            name="child_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="children",
                to="questions.questions",
            ),
        ),
    ]
