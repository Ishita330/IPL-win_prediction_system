from django.urls import path
from .views import IndexView, PredictWinnerView, PredictWithReasoningView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('predict/', PredictWinnerView.as_view(), name='predict'),
    path('predict_with_reasoning/', PredictWithReasoningView.as_view(), name='predict_with_reasoning'),
]
