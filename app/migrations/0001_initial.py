# Generated by Django 5.0.6 on 2024-06-25 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('published_year', models.IntegerField(verbose_name='Год публикации')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('genre', models.CharField(choices=[('Roman', 'Роман'), ('Fantasy', 'Фэнтези'), ('Mystery', 'Детектив'), ('Sci-Fi', 'Научная фантастика'), ('Non-fiction', 'Нон-фикшн')], max_length=50, verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
