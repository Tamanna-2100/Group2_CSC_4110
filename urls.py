from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps import views  # Ensure this matches your app name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page URL
    path('project1/', views.project1, name='project1'),  # Project 1 URL
    path('project2/', views.project2, name='project2'),  # Project 2 URL
    path('project3/', views.project3, name='project3'),  # Project 3 URL
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])