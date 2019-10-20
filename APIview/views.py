from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from classes.models import Classroom
from .serializers import ClassroomSerializer, ClassroomDetailSerializer, ClassroomCreateSerializer, ClassroomUpdateSerializer


class ClassroomList(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomSerializer


class ClassroomDetailView(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailSerializer
	lookup_field = "id"
	lookup_url_kwarg = "classroom_id"

class ClassroomCreate(CreateAPIView):
	serializer_class = ClassroomCreateSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class ClassroomUpdate(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomUpdateSerializer
	lookup_field = "id"
	lookup_url_kwarg = "classroom_id"

class ClassroomDelete(DestroyAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomSerializer
	lookup_field = "id"
	lookup_url_kwarg = "classroom_id"