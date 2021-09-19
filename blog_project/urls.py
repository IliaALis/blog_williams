
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
=======
>>>>>>> bb124a03846794db2f46147dd44dd324bc77ea60
    path('', include('blog.urls')),
]
