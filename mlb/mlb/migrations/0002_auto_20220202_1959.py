# Generated by Django 4.0.2 on 2022-02-02 19:11
from django.db import migrations


def seed(apps, schema_editor):
    Player = apps.get_model('mlb', 'Player')
    Team = apps.get_model('mlb', 'Team')
    red_sox = Team(name='Red Sox', league="American",location="East", wins='54', losses='34')
    rockies = Team(name='Colorado Rockies', league="American",location="Central", wins='45', losses='43')
    braves = Team(name='Atlanta Braves', league="National",location="East", wins='65', losses='54')
    giants = Team(name='San Francisco Giants', league="National", location="West", wins='43', losses='45')
    cubs = Team(name='Chicago Cubs', league="National", location="Central", wins='23', losses='32')

    red_sox.save()
    rockies.save()
    braves.save()
    giants.save()
    cubs.save()

    Player(team=red_sox, name="David Ortiz", age='43', position='DH', injured_list=False).save()
    Player(team=red_sox, name="Donie Booboo", age='29', position='DH', injured_list=False).save()
    Player(team=red_sox, name="Jimmy Dean", age='33', position='DH', injured_list=False).save()
    Player(team=rockies, name="Joseph Chicago Johnson", age='55', position='DH', injured_list=False).save()
    Player(team=rockies, name="Billy Bob Thorton", age='23', position='SS', injured_list=True).save()
    Player(team=rockies, name="Rodney Grey", age='34', position='DH', injured_list=False).save()
    Player(team=braves, name="Moo Snyder", age='44', position='DH', injured_list=False).save()
    Player(team=braves, name="Rostam Rosty Bo", age='53', position='LHP', injured_list=False).save()
    Player(team=braves, name="Christopher Sanchez", age='43', position='DH', injured_list=False).save()
    Player(team=giants, name="James Vazquez", age='55', position='DH', injured_list=True).save()
    Player(team=giants, name="Frankie J", age='52', position='DH', injured_list=False).save()
    Player(team=giants, name="Andre Rodriguez", age='34', position='DH', injured_list=False).save()
    Player(team=cubs, name="Oliver Twist", age='35', position='DH', injured_list=True).save()
    Player(team=cubs, name="Nathaniel BamBam Ortiz", age='36', position='DH', injured_list=False).save()
    Player(team=cubs, name="James Smith", age='41', position='DH', injured_list=False).save()


def fallow(apps, schema_editor):
    Player = apps.get_model('mlb', 'Player')
    Team = apps.get_model('mlb', 'Team')
    Team.objects.app().delete()
    Player.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('mlb', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, fallow)
    ]
