"""
http://pytest-ordering.readthedocs.io/en/develop/
"""

import pytest


# B, A, C, E, D, F
@pytest.mark.run(order=2)
def test_run_order_methodA(one_time_setup, setUp):
    print("Running method A")


@pytest.mark.run(order=1)
def test_run_order_methodB(one_time_setup, setUp):
    print("Running method B")


@pytest.mark.run(order=3)
def test_run_order_methodC(one_time_setup, setUp):
    print("Running method C")


@pytest.mark.run(order=5)
def test_run_order_methodD(one_time_setup, setUp):
    print("Running method D")


@pytest.mark.run(order=4)
def test_run_order_methodE(one_time_setup, setUp):
    print("Running method E")


@pytest.mark.run(order=6)
def test_run_order_methodF(one_time_setup, setUp):
    print("Running method F")

