from django.contrib import admin
from django.urls import path
from prediction.views import IndexView, PredictWinnerView, PredictWithReasoningView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # The IndexView to welcome the API user
    path('api/prediction/', IndexView.as_view()),

    # The route for predicting the winner
    path('api/prediction/predict/', PredictWinnerView.as_view()),

    # The route for predicting the winner with reasoning
    path('api/prediction/predict_with_reasoning/', PredictWithReasoningView.as_view()),
]
