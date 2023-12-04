from rest_framework import serializers
from .models import Voiture, Option, Photo

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class VoitureDetailSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    owner = serializers.StringRelatedField()
    photos = PhotoSerializer(many=True)
    owner_phone = serializers.CharField(source='owner.phone', read_only=True)
    class Meta:
        model = Voiture
        fields = '__all__'


class VoitureSerializer(serializers.ModelSerializer):
    first_photo = serializers.SerializerMethodField()
    owner_phone = serializers.CharField(source='owner.phone', read_only=True)

    class Meta:
        model = Voiture
        fields = ('first_photo', 'owner_phone', 'annee', 'mark', 'model', 'prix', 'kilometrage')

    def get_first_photo(self, obj):
        first_photo = obj.photos.first()
        if first_photo:
            return PhotoSerializer(first_photo).data
        return None
