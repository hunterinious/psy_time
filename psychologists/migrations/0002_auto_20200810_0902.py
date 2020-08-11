# Generated by Django 3.0.7 on 2020-08-10 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('psychologists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='psychologistuserprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.PsychologistUser'),
        ),
        migrations.AddField(
            model_name='psychologisttheme',
            name='profiles',
            field=models.ManyToManyField(related_name='themes', to='psychologists.PsychologistUserProfile'),
        ),
        migrations.AddField(
            model_name='psychologiststatus',
            name='profiles',
            field=models.ManyToManyField(related_name='statuses', to='psychologists.PsychologistUserProfile'),
        ),
        migrations.AddField(
            model_name='psychologistspecialization',
            name='profiles',
            field=models.ManyToManyField(related_name='specializations', to='psychologists.PsychologistUserProfile'),
        ),
        migrations.AddField(
            model_name='psychologistsecondaryeducation',
            name='profiles',
            field=models.ManyToManyField(related_name='secondary_educations', to='psychologists.PsychologistUserProfile'),
        ),
        migrations.AddField(
            model_name='psychologistlanguages',
            name='profiles',
            field=models.ManyToManyField(related_name='languages', to='psychologists.PsychologistUserProfile'),
        ),
        migrations.AddField(
            model_name='psychologisteducation',
            name='profiles',
            field=models.ManyToManyField(related_name='educations', to='psychologists.PsychologistUserProfile'),
        ),
        migrations.AddField(
            model_name='psychologistapproach',
            name='profiles',
            field=models.ManyToManyField(related_name='approaches', to='psychologists.PsychologistUserProfile'),
        ),
        migrations.AddField(
            model_name='image',
            name='profiles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychologists.PsychologistUserProfile'),
        ),
    ]