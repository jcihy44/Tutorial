import pytest
from pytestpackage.class_to_test import SomeClassToTest

@pytest.mark.usefixtures("one_time_setup", "setUp")
class TestReportingDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = SomeClassToTest(10)

    def test_methoda(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running method A")

    def test_methodb(self):
        result = self.abc.sumNumbers(2, 8)
        assert result > 20
        print("Running method B")