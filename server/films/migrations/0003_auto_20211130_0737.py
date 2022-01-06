# Generated by Django 3.2.9 on 2021-11-30 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_auto_20201024_2335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='film',
            options={'ordering': ['title'], 'verbose_name': 'Pelicula'},
        ),
        migrations.AlterModelOptions(
            name='filmgenre',
            options={'ordering': ['name'], 'verbose_name': 'Genero'},
        ),
        migrations.AlterField(
            model_name='film',
            name='genres',
            field=models.ManyToManyField(related_name='film_genres', to='films.FilmGenre', verbose_name='Generos'),
        ),
        migrations.AlterField(
            model_name='film',
            name='image_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='films/', verbose_name='Miniatura'),
        ),
        migrations.AlterField(
            model_name='film',
            name='image_wallpaper',
            field=models.ImageField(blank=True, null=True, upload_to='films/', verbose_name='Wallpaper'),
        ),
        migrations.AlterField(
            model_name='film',
            name='review_large',
            field=models.TextField(blank=True, null=True, verbose_name='Historia(largo)'),
        ),
        migrations.AlterField(
            model_name='film',
            name='review_short',
            field=models.TextField(blank=True, null=True, verbose_name='Argumento(corto)'),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='film',
            name='trailer_url',
            field=models.URLField(blank=True, max_length=150, null=True, verbose_name='URL en Youtube'),
        ),
        migrations.AlterField(
            model_name='film',
            name='year',
            field=models.PositiveBigIntegerField(default=2000, verbose_name='Año'),
        ),
        migrations.AlterField(
            model_name='filmgenre',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
