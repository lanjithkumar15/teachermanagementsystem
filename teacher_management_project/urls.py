from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('show_all_teachers', views.show_all_teachers, name='show_all_teachers'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('filter_teachers/', views.filter_teachers, name='filter_teachers'),
    path('update_teacher/',views.update_teacher,name="update_teacher"),
    path('search_teacher/',views.search_teacher,name="search_teacher"),
    path('delete_record/',views.delete_record,name="delete_record"),
    path('Bonustask/',views.Bonustask,name="Bonustask"),
]
