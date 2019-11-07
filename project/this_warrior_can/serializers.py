from rest_framework import serializers
from this_warrior_can.models import User, TimeSober

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializerSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    birth_date = serializers.DateField()

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password")
        instance.__dict__.update(validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class TimeSoberSerializer(serializers.ModelSerializer):
    time_sober = serializers.SerializerMethodField('get_time_sober')

    class Meta:
        model = TimeSober
        fields = ['title', 'sober_date', 'time_sober']

    def get_time_sober(self, obj):
        return obj.get_time_sober()
