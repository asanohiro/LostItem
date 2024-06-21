# LostAndFound/urls.py
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/app/map/')),  # ルートURLにアクセスしたときにリダイレクト
    path('app/', include('app.urls')),  # 'app' アプリケーションのURLパターンを追加
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
