
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
import logging
from tasks import views


logger = logging.getLogger(__name__)

def health_check(request):
    """
    Basic health check endpoint that always returns HTTP 200.
    This is used by Koyeb to determine if the application is running.
    """
    logger.info("Health check request received")
    return HttpResponse("OK", status=200)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='tasks/logout.html', next_page='/'), name='logout'),
    path('health/', health_check, name='health_check'),
   
]




# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
