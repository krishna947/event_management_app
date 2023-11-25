from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Event
from .serializers import EventSerializer
from .permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework import status


class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class EventUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class EventSummaryView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)