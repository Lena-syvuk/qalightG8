#Task_2
import pytest


@pytest.fixture(autouse=False)
def global_lecture_pytest_fixture():
    print('global_lecture_pytest_fixture setup')
    yield
    print('global_lecture_pytest_fixture teardown')


