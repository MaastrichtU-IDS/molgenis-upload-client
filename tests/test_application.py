import pytest

from molgenis_upload_client.application import App


@pytest.fixture
def app():
    return App()


class TestApplication(object):

    def test_return_value(self, app):
        assert app.get_hello_world() == "Hello, World"