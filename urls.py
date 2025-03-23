from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),  # ✅ Add namespace
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),  # ✅ Add namespace
    path('', TemplateView.as_view(template_name='mr_makeit/home.html'), name='home'),
]
