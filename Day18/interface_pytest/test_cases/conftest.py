import pytest

from Day18.interface_pytest.api_keys.api_keys import ApiKeys
from Day18.interface_pytest.conf.set_cof import write_ini_conf


@pytest.fixture(scope='session')
def api():
    api = ApiKeys()
    return api


@pytest.fixture(scope='session')
def set_api_env(request, api):
    env = request.param
    api.set_env(env)


@pytest.fixture(scope='session')
def clean_data(request):
    def clean_data_finalizer():
        write_ini_conf('common_parm.ini', data={'token': '', 'id': '', 'user_id': ''})

    request.addfinalizer(clean_data_finalizer)

