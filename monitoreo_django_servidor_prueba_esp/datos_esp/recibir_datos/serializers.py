from rest_framework import serializers
from recibir_datos.models import VoltajeCorriente


class VoltajeCorrienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoltajeCorriente
        fields = ['id', 'voltaje', 'corriente']