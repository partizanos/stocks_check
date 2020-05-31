from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('/stocks_json_file', views.home),
    path('product/<id_product>', views.view_article),
    path('search_stocks/<queue_word>', views.search_stocks),

]