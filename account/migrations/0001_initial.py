# Generated by Django 4.2.6 on 2023-11-16 09:37

import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome categoria')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_nascita', models.DateField(blank=True, null=True, verbose_name='Data di nascita')),
                ('cf', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message='Inserisci un CF valido', regex='^[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}$')], verbose_name='Codice fiscale')),
                ('tipo_account', models.CharField(choices=[('admin', 'Admin'), ('developer', 'Developer'), ('cliente', 'Cliente'), ('magazziniere', 'Magazziniere')], default='cliente', max_length=50, verbose_name='Tipologia utente')),
                ('img_profilo', imagekit.models.fields.ProcessedImageField(default='user_profile/profile_user.png', upload_to='user_profile/%Y/%m/%d/')),
                ('indirizzo', models.CharField(blank=True, max_length=250, null=True)),
                ('comune', models.CharField(blank=True, max_length=200, null=True)),
                ('citta', models.CharField(blank=True, max_length=150, null=True)),
                ('cap', models.CharField(blank=True, max_length=5, null=True, validators=[django.core.validators.RegexValidator(message='Inserisci un cap valido', regex='^[0-9]{5}$')], verbose_name='C.A.P.')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=200, verbose_name='Titolo della slide')),
                ('sottotitolo', models.CharField(blank=True, max_length=250, null=True, verbose_name='Sottotitolo della slide')),
                ('corpo', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Contenuto dello slide')),
                ('img', models.ImageField(blank=True, null=True, upload_to='slide/%Y/%m/', verbose_name='Immagine Slide')),
                ('pubblicato', models.BooleanField(default=False, verbose_name='Pubblicato')),
                ('categoria', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='account.categoriacarousel')),
            ],
        ),
    ]
