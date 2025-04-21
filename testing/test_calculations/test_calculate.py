from calculations.calculate import calculate


def test_calculate():
    """
    Test calculate: success
    """
    assert 9 == calculate('(1 + 2)*3')