#Method name should have sense
# -k stands for method names execution, -s logs in output and -v stands for more info metadata
# you can run specific file with py.test <filename>
# -m stands for mark, you can mark (tag) tests @pytest.mark.<name_of_mark>
#@p.mark.xfail

import pytest


@pytest.mark.smoke
def test_program():
    a = 5
    b = 10
    assert a+5 == 10, "addition do not match"


@pytest.mark.xfail
def test_ProgramOnlineBanking():
    a = 4
    b = 6
    assert a+2 == b, "Addition failed"

