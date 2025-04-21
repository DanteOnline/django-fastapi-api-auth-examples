import random


def get_random_expression(
        operations_count: int = 2,
        operations_list: list = None,
        max_number: int = 10):
    operations_list = operations_list if operations_list else ['*', '/', '+', '-']
    first = random.randint(1, max_number)
    result_expression = ''
    for _ in range(operations_count):
        random_operation = random.choice(operations_list)
        second = random.randint(1, max_number)
        result_expression = f'({first}{random_operation}{second})'
        first = result_expression
    return result_expression
