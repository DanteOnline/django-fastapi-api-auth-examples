from rest_framework.decorators import api_view
from rest_framework.response import Response
from calculations.calculate import calculate
from calculations.expression import get_random_expression


@api_view(['POST'])
def calculate_api_view(request):
    expression = request.data['expression']
    result = calculate(expression)
    return Response({"result": result})


@api_view(['GET'])
def random_expression_api_view(request):
    expression = get_random_expression()
    return Response({"expression": expression})
