from django.urls import path
from .views import calculate_api_view, random_expression_api_view


urlpatterns = [
    path('calculate/', calculate_api_view),
    path('random-expression/', random_expression_api_view),
]
