from . import views
from django.urls import path
app_name='movieapp'

urlpatterns = [

    path('',views.movie,name='movie'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('addm/',views.addm,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]