from aloe import before, step, world
from aloe.tools import guess_types
from aloe_django.steps.models import get_model
from nose.tools import assert_true, assert_equal
from django.http import QueryDict

from urllib.parse import urlencode

from rest_framework.test import APIClient

from this_warrior_can.models import User
from this_warrior_can.serializers import UserSerializerSerializer


def make_post_request(data):
    return world.client.post(
        '/create_user/',
        urlencode(data),
        content_type='application/x-www-form-urlencoded')

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
    world.response = make_post_request(world.data)

@step('I am redirected to login')
def step_assert_redirect(self):
    assert_equal(world.response.status_code, 302)
    assert_equal(world.response.url, '/account/login/')

@step('The user is found in the database')
def step_assert_in_database(self):
    assert_true(User.objects.get(username=world.username))

@step('I empty the "([^"]+)" table')
def step_empty_table(self, model_name):
    get_model(model_name).objects.all().delete()

@step('I create the following users:')
def step_create_users(self):
    for user in guess_types(self.hashes):
        User.objects.create_user(**user)

@step('I create a user with the same username')
def step_create_user_with_same_username(self):
    world.response = make_post_request(world.data)

@step('An exception is not raised')
def step_check_for_exception(self):
    assert_equal(world.response.status_code, 200)
    assert_equal(User.objects.all().count(), 1)

@step('I submit an invalid email')
def step_submit_invalid_email(self):
    invalid_data = world.data
    invalid_data['email'] = 'notvalid'
    world.response = make_post_request(invalid_data)

@step('I omit first name')
def step_omit_required_field(self):
    invalid_data = world.data
    del invalid_data['first_name']
    world.response = make_post_request(invalid_data)

@step('No user is created')
def step_check_not_created(self):
    assert_equal(world.response.status_code, 200)
    assert_equal(User.objects.all().count(), 0)
