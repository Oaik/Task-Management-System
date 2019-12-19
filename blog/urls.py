from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as articleView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("articles/", include("articles.urls")),
    path("account/", include('accounts.urls')),
    path("", articleView.article_list)
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
