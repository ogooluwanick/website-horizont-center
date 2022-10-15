# Generated by Django 4.1.2 on 2022-10-15 14:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('first_name', models.CharField(max_length=20, verbose_name='first name')),
                ('last_name', models.CharField(max_length=20, verbose_name='last name')),
                ('description', models.TextField(validators=[django.core.validators.MinLengthValidator(limit_value=100)], verbose_name='description')),
                ('facebook_url', models.URLField(verbose_name='facebook url')),
                ('image', models.ImageField(upload_to='image/blogAuthors', verbose_name='image')),
                ('instagram_url', models.URLField(verbose_name='instagram url')),
            ],
            options={
                'verbose_name': 'Blog Author',
                'verbose_name_plural': 'Blog Authors',
            },
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('color', models.CharField(max_length=100, verbose_name='color')),
            ],
            options={
                'verbose_name': 'Blog Category',
                'verbose_name_plural': 'Blog Categories',
            },
        ),
        migrations.CreateModel(
            name='BlogSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(limit_value=100)], verbose_name='description')),
                ('media_url', models.URLField(blank=True, null=True, verbose_name='media url')),
                ('media_type', models.CharField(choices=[('facebook', 'facebook'), ('instagram', 'instagram')], max_length=100, verbose_name='media type')),
            ],
            options={
                'verbose_name': 'Blog Section',
                'verbose_name_plural': 'Blog Sections',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/blogs', verbose_name='image')),
                ('blog_author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blogs.blogauthor', verbose_name='blog author')),
                ('blog_category', models.ManyToManyField(to='blogs.blogcategory', verbose_name='blog category')),
                ('blog_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.blogsection', verbose_name='blog section')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]