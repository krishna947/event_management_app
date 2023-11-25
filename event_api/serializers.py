from rest_framework import serializers
from .models import Event, Booking
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = CustomUser
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class BookingEventSerializer(serializers.Serializer):
    event_id = serializers.IntegerField()