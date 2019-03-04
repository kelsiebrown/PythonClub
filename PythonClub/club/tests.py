from django.test import TestCase
from .models import Meeting, Resource, Event
from .forms import ResourceForm, MeetingForm
from datetime import datetime
from django.urls import reverse

### Class tests ###
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


### View tests ###
# testing index view
class TestIndexView(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'club/index.html')

# testing details view
class TestResourceView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/club/resources')
        self.assertEqual(response.status_code, 200)
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('resources'))
        self.assertTemplateUsed(response, 'club/resources.html')

# testing meetings view
class TestMeetingView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/club/meetings')
        self.assertEqual(response.status_code, 200)
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('meetings'))
        self.assertTemplateUsed(response, 'club/meetings.html')


### Form tests ###
# testing add resource form
class New_Resource_Form_Test(TestCase):
    def test_resourceForm_is_valid(self):
        form = ResourceForm(data={'resourcename': "Events", 'resourcetype': "event", 'resourceurl': "http://www.pythonevents.com", 'dateentered': "2019-01-30", 'user':"kbrown", 'resourcedescription':"Events that Python Club members may be interested in" })
        self.assertTrue(form.is_valid())
    def test_resourceForm_invalid(self):
        form = ResourceForm(data={'resourcename': "Events", 'resourcetype': "event", 'resourceurl': "http://www.pythonevents.com", 'dateentered': "2019-01-30", 'user':"kbrown", 'resourcedescription':"Events that Python Club members may be interested in" })
        self.assertFalse(form.is_valid())

# testing add meeting form
class New_Meeting_Form_Test(TestCase):
    def test_meetingForm_is_valid(self):
        form = MeetingForm(data={'meetingtitle' : 'Feb Monthly Meeting', 'meetingdate' : '2019-02-27', 'meetingtime' : '18:00:00', 'location' : 'Club room', 'agenda' : 'Feb monthly meeting agenda' })
        self.assertTrue(form.is_valid())
    def test_meetingForm_invalid(self):
        form = MeetingForm(data={'meetingtitle' : 'Feb Monthly Meeting', 'meetingdate' : '2019-02-27', 'meetingtime' : '18:00:00', 'location' : 'Club room', 'agenda' : 'Feb monthly meeting agenda' })
        self.assertFalse(form.is_valid())

