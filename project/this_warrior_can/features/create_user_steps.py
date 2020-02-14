from aloe import before, step, world
from aloe.tools import guess_types
from aloe_django.steps.models import get_model
from nose.tools import assert_true, assert_equal
from django.http import QueryDict

from urllib.parse import urlencode

from rest_framework.test import APIClient

from this_warrior_can.models import User
from this_warrior_can.serializers import UserSerializerSerializer

@before.each_feature
def before_each_feature(feature):
    world.client = APIClient()
    world.username = 'test'
    world.password = 'pswd124'
    world.data = {
        'email': 'test@gmail.com',
        'username': world.username,
        'password': world.password,
        'first_name': 'test',
        'last_name': 'ing',
        'birth_date': '1992-02-25',
    }

@step('I fill out all the required fields')
def complete_form(self):
    world.response = world.client.post(
        '/create_user/',
        urlencode(world.data),
        content_type='application/x-www-form-urlencoded')

@step('I am redirected to login')
def step_assert_redirect(self):
    assert_equal(world.response.status_code, 302)
    assert_equal(world.response.url, '/account/login/')

@step('The user is found in the database')
def step_assert_in_database(self):
    assert_true(User.objects.get(username=world.username))
