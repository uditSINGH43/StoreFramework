# Any pytest file should start with "test_"
#all work done in pytest will be done in function/method.
#test method names should start with test
# you can skip test with @pytest.mark.skip

import pytest



@pytest.mark.smoke
def test_firstOnlineBanking(setup):
    print("Hello")

@pytest.mark.skip
def test_Greetings():
    msg = "Good Morning"
    assert msg == "hey", "test failed"


def test_crossBrowser(crossBrowser):
    print(crossBrowser)