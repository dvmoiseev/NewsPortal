from django.contrib import admin
from django.urls import path, include
from news.views import subscribe

urlpatterns = [
    path('pages/', include('django.contrib.flatpages.urls')),
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('news/', include('news.urls')),
    path('categories/<int:pk>/subscribe', subscribe),
    path('', include('news.urls')),
]
