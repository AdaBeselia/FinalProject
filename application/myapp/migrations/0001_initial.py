# Generated by Django 5.0.3 on 2024-03-28 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=255)),
                ('abstract', models.TextField()),
                ('project_duration', models.IntegerField(choices=[(2, 2), (3, 3)])),
                ('field', models.CharField(choices=[('Natural studies', 'Natural studies'), ('Engineering and technology', 'Engineering and technology'), ('Medical and health sciences', 'Medical and health sciences'), ('Agricultural sciences', 'Agricultural sciences'), ('Social sciences', 'Social sciences'), ('Humanities', 'Humanities')], max_length=50)),
                ('keywords', models.TextField()),
                ('undesirable_expert', models.CharField(max_length=100)),
            ],
        ),
    ]