from rest_framework import serializers

from caieiras.model import caieiras

class CaieirasSerializer(serializers.ModelSerializer):
    class Meta:
        model = caieiras
        fields =('id', 'nome_musica', 'nome_cantor', 'genero_musical')