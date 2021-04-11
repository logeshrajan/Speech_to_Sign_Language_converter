from django.urls import path
from .views import *
urlpatterns = [
    # path('',views.index,name='index'),
    # path('record',views.index,name='record'),
    path('',AjaxHandlerView.as_view())

]