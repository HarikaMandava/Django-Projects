from django.urls import path
from . import views

'''urlpatterns = [
    path('',views.home,name='home'),
    path('vendor/', views.addvendor,name='addvendor'),
    path('contacts/', views.addcontact,name='addcontact'),
]'''
urlpatterns = [
    path('create/', views.create,name='create'),
    path('<int:vendor_id>', views.detail, name='detail'),
    path('contact/', views.contact,name='contact'),
    path('contact_detail/', views.contact_detail, name='contact_detail'),
    path('vendor_details/', views.vendor_details,name='vendor_details'),
    path('vendor_contacts/', views.vendor_contacts,name='vendor_contacts'),
]