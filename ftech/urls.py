from ftech import views
from django.urls import path

urlpatterns=[
    path('',views.render_index,name='render_index'),
    path('register/',views.register_page,name='register'),
    path('perform_registration/',views.perform_registration,name='perform_registration'),
    path('submit_form/',views.submit_form,name='submit_form'),
    path('logout_view/',views.logout_view,name='logout_view'),
    path('home/',views.home,name='home'),
    path('login/',views.render_login,name='login'),
    path('perform_login',views.perform_login,name='perform_login'),
]