# Generated by Django 3.1.4 on 2020-12-11 00:39

from django.db import migrations


def copy_columns(apps, schema_editor):
    Exercise = apps.get_model('exercises', 'Exercise')
    ExerciseBase = apps.get_model('exercises', 'ExerciseBase')

    for exercise in Exercise.objects.all():
        exercise_base = ExerciseBase.objects.create(
            category=exercise.category,
        )
        exercise_base.equipment.set(exercise.equipment.all())
        exercise_base.muscles.set(exercise.muscles.all())
        exercise_base.muscles_secondary.set(exercise.muscles_secondary.all())
        exercise_base.status = exercise.status
        exercise_base.license = exercise.license
        exercise_base.license_author = exercise.license_author
        exercise_base.license_author = exercise.license_author
        exercise_base.variations = exercise.variations
        exercise_base.save()

        exercise.exercise_base = exercise_base
        exercise.save()


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0008_exercisebase'),
    ]

    operations = [
        migrations.RunPython(copy_columns),
    ]
