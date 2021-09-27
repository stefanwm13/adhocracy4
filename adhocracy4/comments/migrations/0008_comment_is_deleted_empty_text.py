# Generated by Django 2.2.24 on 2021-09-30 07:32

from django.db import migrations


def forwards_func(apps, schema_editor):
    Comment = apps.get_model("a4comments", "Comment")
    for comment in Comment.objects.all():
        if comment.is_censored or comment.is_removed:
            comment.comment = ''
            comment.save()


def reverse_func(apps):
    Comment = apps.get_model("a4comments", "Comment")
    for comment in Comment.objects.all():
        if comment.is_censored:
            comment.comment = 'deleted by moderator'
            comment.save()
        elif comment.is_removed:
            comment.comment = 'deleted by creator'
            comment.save()


class Migration(migrations.Migration):

    dependencies = [
        ('a4comments', '0007_comment_is_moderator_marked'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
