from django.contrib import admin
from django.urls import path
from Blog.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view()),
    path('shaxar/', Portfolio.as_view()),
    path('muhandis/', Contact.as_view()),
    path('din/', Services.as_view()),
    path('blog/', Blog.as_view()),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)










