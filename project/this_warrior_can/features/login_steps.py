from aloe import before, step, world
from aloe.tools import guess_types
from aloe_django.steps.models import get_model
from nose.tools import assert_true, assert_equal

from this_warrior_can.models import User

from rest_framework.test import APIClient

@before.each_feature
def before_each_feature(feature):
    world.client = APIClient()

@step('I access the url "/"')
def step_access_url(self):
    world.response = world.client.get('/')

@step('I am redirected to the login page')
def step_assert_redirect_and_next_url(self):
    assert_equal(world.response.status_code, 302)
    assert_equal(world.response.url, "/account/login/?next=/")

@step('I empty the "([^"]+)" table')
def step_empty_table(self, model_name):
    get_model(model_name).objects.all().delete()

@step('I create the following users:')
def step_create_users(self):
    for user in guess_types(self.hashes):
        User.objects.create_user(**user)

@step('I log in with username "([^"]+)" and password "([^"]+)"')
def step_login(self, username, password):
    world.is_logged_in = world.client.login(username=username, password=password)

@step('I am logged in')
def step_confim_login(self):
    assert_true(world.is_logged_in)
