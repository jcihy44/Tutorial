import pytest


@pytest.fixture()
def setup():
    print("Running demo1 setUp")


def test_demo1_methoda(setup):
    print("Running demo1 method A")


def test_demo1_methodb(setup):
    print("Running demo1 method B")
