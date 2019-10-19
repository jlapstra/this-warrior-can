from rest_framework import serializers
from this_warrior_can.models import User, TimeSober

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class TimeSoberSerializer(serializers.ModelSerializer):
    time_sober = serializers.SerializerMethodField('get_time_sober')

    class Meta:
        model = TimeSober
        fields = ['title', 'sober_date', 'time_sober']

    def get_time_sober(self, obj):
        return obj.get_time_sober()
