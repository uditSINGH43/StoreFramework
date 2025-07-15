#this file should name as 'conftest.py' always, and it is used as a common fixture for all other test cases
# fixture are used as a setup and tear down methods for test cases- confest file is generalized
# datadriver and paramerterization can be done with return statements in tuple format
# when u define fixture scope to class only, it will run once before class is initiated and at the end
import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will be executing first")
    yield
    print("i will be executing last")

@pytest.fixture()
def dataLoad():
    print("data is here")
    return ["Udit", "Singh", "2004udit@gmai.com"]

@pytest.fixture(params=["Crome", "Firefox", "IE"])
def crossBrowser(request):
    return request.param
