from django.urls import path
from .views import EventCreateView, EventListView, EventUpdateView, EventSummaryView, CustomUserCreate
from .user_views import EventListView, BookEventView, UserBookingsView, AllUserEventsView

urlpatterns = [
    path('events/create/', EventCreateView.as_view(), name='event-create'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('events/<int:pk>/summary/', EventSummaryView.as_view(), name='event-summary'),


    path('register/', CustomUserCreate.as_view(), name="create_user"),


    path('allevents/', EventListView.as_view(), name='event-list'),
    path('events/book/', BookEventView.as_view(), name='event-book'),
    path('user/bookings/', UserBookingsView.as_view(), name='user-bookings'),
    path('user/events/', AllUserEventsView.as_view(), name='user-events'),    
]
