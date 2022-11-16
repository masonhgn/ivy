# Generated by Django 4.1.2 on 2022-11-16 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='logo',
        ),
        migrations.AddField(
            model_name='company',
            name='logo_url',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='company',
            name='url',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='companyreview',
            name='star_rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=10),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='stage',
            field=models.CharField(choices=[('Applied', 'Applied'), ('Rejected', 'Rejected'), ('Online Assessment', 'Online Assessment'), ('1st Round Interview', '1st Round Interview'), ('2nd Round Interview', '2nd Round Interview'), ('3rd Round Intervew', '3rd Round Intervew'), ('4th Round Interview', '4th Round Interview'), ('Given Offer', 'Given Offer')], max_length=19),
        ),
    ]