import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoOne.settings')

import django
django.setup()

#Fake Pop Script

import random
from firs_app.models import Topic, Webpage, Accesrecord
from faker import Faker

Fakegen = Faker()

topics= [ "Social", " Search", "Marketplace", "News", "Games"]

def add_topic():
    t=Topic.objects.get_or_create(topname=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):
    #get the topic for the entry
        top = add_topic()

        #create fake data for the entry
        fake_url = Fakegen.url()
        fake_date = Fakegen.date()
        fake_name = Fakegen.company()

        #create a new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        #create a fake access record
        acc_rec = Accesrecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("Populating script...")
    populate(20)
    print("Populating complete!")