from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username', 'first_name', 'last_name', 'phone_number', 'email', 'password']
        
        def validate(self, attrs):
            # Verifica si la solicitud es un POST
            if self.context['request'].method == 'POST':
            # Asegúrate de que los campos requeridos estén presentes
                if 'email' not in attrs or not attrs['email']:
                    raise serializers.ValidationError({'email': 'Este campo es obligatorio.'})
                if 'username' not in attrs or not attrs['username']:
                    raise serializers.ValidationError({'username': 'Este campo es obligatorio.'})
                if 'password' not in attrs or not attrs['password']:
                    raise serializers.ValidationError({'password': 'Este campo es obligatorio.'})
            return attrs
               
        
