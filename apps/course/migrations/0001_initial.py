# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-14 14:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='购买时间')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='课程名称')),
                ('price', models.IntegerField(default=0, verbose_name='价格')),
                ('learn_time', models.CharField(max_length=6, verbose_name='学习时长')),
                ('nums', models.IntegerField(default=0, verbose_name='购买人数')),
                ('image', models.ImageField(upload_to='img/%Y/%m', verbose_name='封面图')),
                ('describe', models.ImageField(upload_to='img/course/%Y/%m', verbose_name='描述')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击人数')),
            ],
            options={
                'verbose_name_plural': '课程',
                'verbose_name': '课程',
            },
        ),
        migrations.CreateModel(
            name='CourseClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('it', 'IT互联网'), ('language', '语言留学'), ('design', '创意设计'), ('life', '兴趣生活'), ('plant', '生产种植'), ('edu', '升学考研'), ('certificate', '公培考证')], max_length=15, verbose_name='分类')),
            ],
            options={
                'verbose_name_plural': '第一分类',
                'verbose_name': '第一分类',
            },
        ),
        migrations.CreateModel(
            name='CourseSort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='第二分类')),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseClass', verbose_name='第一分类')),
            ],
            options={
                'verbose_name_plural': '第二分类',
                'verbose_name': '第二分类',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='课程名')),
                ('start_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='开始时间')),
                ('end_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='结束时间')),
                ('lesson_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='课程')),
            ],
            options={
                'verbose_name_plural': '章节',
                'verbose_name': '章节',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=30, verbose_name='老师名')),
                ('teacher_des', models.CharField(max_length=100, verbose_name='老师描述')),
                ('teacher_img', models.ImageField(upload_to='img/tea/&Y/%m', verbose_name='老师图')),
                ('teacher_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='课程名')),
            ],
            options={
                'verbose_name_plural': '老师',
                'verbose_name': '老师',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='sort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseSort', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='buy',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='课程'),
        ),
    ]
