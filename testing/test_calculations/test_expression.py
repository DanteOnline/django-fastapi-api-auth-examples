from unittest import mock
from calculations.expression import get_random_expression


def test_get_random_expression_str():
    """
    Test get_random_expression: success result is str
    """
    assert isinstance(get_random_expression(
        operations_count=2,
        operations_list=['+', '*'],
        max_number=100,
    ), str)


def test_get_random_expression_has_one_operation():
    """
    Test get_random_expression: success result has one operation
    """
    assert '+' in get_random_expression(
        operations_count=1,
        operations_list=['+'],
        max_number=100,
    )

def test_get_random_expression():
    """
    Test get_random_expression: success
    """
    with mock.patch('random.randint') as mock_randint:
        mock_randint.return_value = 5
        with mock.patch('random.choice') as mock_choice:
            mock_choice.return_value = '*'
            assert '((5*5)*5)' == get_random_expression(
                operations_count=2,
                operations_list=['+', '-', '*'],
                max_number=10,
            )
