


from django.contrib import admin
# importing path and include from django's in-built urls
from django.urls import path, include

# defining the list for urls
urlpatterns = [
    path('admin/', admin.site.urls),
    # registering dictionary app urls in project
    path('', include('dictionary.urls')),
]




