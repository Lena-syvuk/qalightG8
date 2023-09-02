#Task_4
import pytest


@pytest.fixture(autouse=True)
def global_lecture_pytest_fixture_auto():
    print('global_lecture_pytest_fixture setup auto')
    yield
    print('global_lecture_pytest_fixture teardown auto')


@pytest.fixture(autouse=False)
def digit():
    yield 5

