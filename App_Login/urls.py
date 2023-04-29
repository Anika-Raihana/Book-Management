from django.urls import path
from App_Login import views
app_name='App_Login'


urlpatterns=[
    path('DataEntryForm/',views.data_entry, name='DataEntryForm'),

]
