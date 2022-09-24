from django.urls import path
from .adminviews import CalculatorView

urlpatterns = [path("calculator/", CalculatorView.as_view(), name="calculator-view"),
                ]
