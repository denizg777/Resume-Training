from django.urls import path
from .views import index, contact, services, about, work, work_single, work_single_2, work_single_3
from .views import work_single_4, work_single_5, work_single_6, work_single_7, redirect_urls

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('services', services, name='services'),
    path('about', about, name='about'),
    path('work', work, name='work'),
    path('work-single', work_single, name='work-single'),
    path('work-single-2', work_single_2, name='work-single-2'),
    path('work-single-3', work_single_3, name='work-single-3'),
    path('work-single-4', work_single_4, name='work-single-4'),
    path('work-single-5', work_single_5, name='work-single-5'),
    path('work-single-6', work_single_6, name='work-single-6'),
    path('work-single-7', work_single_7, name='work-single-7'),

    path('<slug>/', redirect_urls, name='redirect_urls' ),

]