import pytest
from pytestpackage.class_to_test import SomeClassToTest


@pytest.mark.usefixtures("one_time_setup", "setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self, one_time_setup):
        self.abc = SomeClassToTest(self.value)

    def test_methoda(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running method A")

    def test_methodb(self):
        print("Running method B")