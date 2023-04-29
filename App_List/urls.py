from django.urls import path
from App_Login import views
app_name='App_List'


urlpatterns=[
    path('booklist/<pk>/',views.booklist, name='booklist'),
]
