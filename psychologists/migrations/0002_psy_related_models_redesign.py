# Generated by Django 3.0.7 on 2020-08-12 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychologists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PsychologistLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='psychologistapproach',
            name='profiles',
        ),
        migrations.RemoveField(
            model_name='psychologisteducation',
            name='profiles',
        ),
        migrations.RemoveField(
            model_name='psychologistsecondaryeducation',
            name='profiles',
        ),
        migrations.RemoveField(
            model_name='psychologistspecialization',
            name='profiles',
        ),
        migrations.RemoveField(
            model_name='psychologiststatus',
            name='profiles',
        ),
        migrations.RemoveField(
            model_name='psychologisttheme',
            name='profiles',
        ),
        migrations.RemoveField(
            model_name='psychologistworkformat',
            name='profiles',
        ),
        migrations.AddField(
            model_name='psychologistuserprofile',
            name='approaches',
            field=models.ManyToManyField(related_name='profiles', to='psychologists.PsychologistApproach'),
        ),
        migrations.AddField(
            model_name='psychologistuserprofile',
            name='educations',
            field=models.ManyToManyField(related_name='profiles', to='psychologists.PsychologistEducation'),
        ),
        migrations.AddField(
            model_name='psychologistuserprofile',
            name='formats',
            field=models.ManyToManyField(related_name='profiles', to='psychologists.PsychologistWorkFormat'),
        ),
        migrations.AddField(
            model_name='psychologistuserprofile',
            name='secondary_educations',
            field=models.ManyToManyField(related_name='profiles', to='psychologists.PsychologistSecondaryEducation'),
        ),
        migrations.AddField(
            model_name='psychologistuserprofile',
            name='specializations',
            field=models.ManyToManyField(related_name='profiles', to='psychologists.PsychologistSpecialization'),
        ),
        migrations.AddField(
            model_name='psychologistuserprofile',
            name='statuses',
            field=models.ManyToManyField(related_name='profiles', to='psychologists.PsychologistStatus'),
        ),
        migrations.AddField(
            model_name='psychologistuserprofile',
            name='themes',
            field=models.ManyToManyField(related_name='profiles', to='psychologists.PsychologistTheme'),
        ),
        migrations.DeleteModel(
            name='PsychologistLanguages',
        ),
        migrations.AddField(
            model_name='psychologistuserprofile',
            name='languages',
            field=models.ManyToManyField(related_name='profiles', to='psychologists.PsychologistLanguage'),
        ),
    ]