from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse

# test Meeting class
class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting=Meeting(meetingtitle='Club member party')
        self.assertEqual(str(meeting), meeting.meetingtitle)
    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

# test Resource class
class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource=Resource(resourcename='resource')
        self.assertEqual(str(resource), resource.resourcename)
    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')
    
# test Event class
class EventTest(TestCase):
    def test_stringOutput(self):
        event=Event(eventtitle='event title')
        self.assertEqual(str(event), event.eventtitle)
    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')