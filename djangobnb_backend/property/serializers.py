from rest_framework import serializers

from .models import Property


class PropertiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = (
            'id',
            'title',
            'price_per_night',
            'image_url',
        )
    
    def get_image_url(self, obj):
        # This executes the property model's image_url method 
        # to get the actual string URL.
        return obj.image_url()