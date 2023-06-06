from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('success/',views.success,name='success'),
    path('form-admin',views.form_admin,name='form-admin')
]
