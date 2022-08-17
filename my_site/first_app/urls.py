from django.urls import path
from . import views

#path looks empty '' but gets the path from the project urls being first_app
urlpatterns = {
    path('<str:topic>/', views.news_view),
    path('<int:num1>/<int:num2>',views.add_view)
}