from rest_framework import generics
from rest_framework.response import Response
from .models import Event, Booking
from .serializers import EventSerializer, BookingSerializer, BookingEventSerializer
from rest_framework.views import APIView
from .models import Booking
from rest_framework import status

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all().order_by('booking_open_window_start')
    serializer_class = EventSerializer

# class BookEventView(generics.CreateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer


class BookEventView(APIView):
    def post(self, request, format=None):
        user = self.request.user
        serializer = BookingEventSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'error': 'Bad request', 'msg': 'error'}, status=status.HTTP_400_BAD_REQUEST) 
      
        try:
            id = serializer.validated_data.get('event_id')
            event = Event.objects.get(id=id)
            if not event.is_booking_open():
                return Response({'msg': 'Booking is not open for this event'}, status=status.HTTP_200_OK)
            booking = Booking.objects.create(user=user, event_id=id)      
        except Exception as e:
            return Response({'error': str(e), 'msg': 'Error in creating booking'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': 'Booking Event successfull'}, status=status.HTTP_200_OK)


class UserBookingsView(generics.ListAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        user = self.request.user
        return Booking.objects.filter(user=user)


class AllUserEventsView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(booking__user=user).order_by('booking_open_window_start')
