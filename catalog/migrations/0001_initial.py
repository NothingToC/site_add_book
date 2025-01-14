# Generated by Django 3.0.9 on 2024-06-10 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Enter author first name', max_length=100, verbose_name='Author first name')),
                ('last_name', models.CharField(help_text='Enter author last name', max_length=100, verbose_name='Author last name')),
                ('date_of_birth', models.DateField(blank=True, help_text='Enter birth date', null=True, verbose_name='Date of birth')),
                ('date_of_death', models.DateField(blank=True, help_text='Enter death date', null=True, verbose_name='Date of death')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text="Enter book's name", max_length=200, verbose_name="Book's name")),
                ('summary', models.TextField(help_text='Enter summary for book', max_length=1000, verbose_name="Book's summary")),
                ('isbn', models.CharField(help_text="it's should to consist of 13 charcaters", max_length=13, verbose_name="Book's ISBN")),
                ('author', models.ManyToManyField(help_text="Choose book's author", to='catalog.Author', verbose_name="Book's author")),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter book genre's", max_length=200, verbose_name="Book's genre")),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter book's language", max_length=20, verbose_name="Book's language")),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter book's status", max_length=20, verbose_name="Book's status")),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_nom', models.CharField(help_text="Enter book's inventory number", max_length=20, verbose_name='Inventory number')),
                ('imprint', models.CharField(help_text='Enter publisher and year of issue', max_length=200, verbose_name='Publisher')),
                ('due_back', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Book')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Status')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(help_text='Choose genre for book', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Genre', verbose_name="Book's genre"),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='Choose language for book', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Language', verbose_name="Book's language"),
        ),
    ]
