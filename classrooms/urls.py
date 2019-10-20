
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views as classes
from APIview import views as api
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', classes.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', classes.classroom_detail, name='classroom-detail'),

    path('classrooms/create', classes.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', classes.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', classes.classroom_delete, name='classroom-delete'),

	path('login/', TokenObtainPairView.as_view(), name="login"),

    path('api/classrooms/', api.ClassroomList.as_view()),
    path('api/classrooms/<int:classroom_id>/', api.ClassroomDetailView.as_view()),

    path('api/classrooms/create/', api.ClassroomCreate.as_view()),
    path('api/classrooms/<int:classroom_id>/update/', api.ClassroomUpdate.as_view()),
    path('api/classrooms/<int:classroom_id>/delete/', api.ClassroomDelete.as_view()),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
