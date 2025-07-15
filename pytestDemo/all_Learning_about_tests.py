# Any pytest file should start with "test_"
#all work done in pytest will be done in function/method.
#test method names should start with test
# you can skip test with @pytest.mark.skip
#Method name should have sense
# -k stands for method names execution, -s logs in output and -v stands for more info metadata
# you can run specific file with py.test <filename>
# -m stands for mark, you can mark (tag) tests @pytest.mark.<name_of_mark>
#@p.mark.xfail
#this file should name as 'conftest.py' always, and it is used as a common fixture for all other test cases
# fixture are used as a setup and tear down methods for test cases- confest file is generalized
# datadriver and paramerterization can be done with return statements in tuple format
# when u define fixture scope to class only, it will run once before class is initiated and at the end