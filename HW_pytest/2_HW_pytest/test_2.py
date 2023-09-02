#Task_4
def test_1():
    print('lecture_pytest test executed')


def test_2(global_lecture_pytest_fixture):
    print('lecture_pytest test executed')


def test_3(digit,global_lecture_pytest_fixture):
    print(type(digit))