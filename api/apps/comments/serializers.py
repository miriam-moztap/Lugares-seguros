from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'place',
            'comment',
            'created',
        )

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'place': {
                'id': instance.place.id,
                'name': instance.place.name
            },
            'comment': instance.comment,
            'created': instance.created
        }
    
    #ahora, en lugar de listar toda la información de arriba, vamos a crear un serializador que minimice la inf y sólo mostrar el id y el nombre del lugar, porque ahora queremos listar todos los ocmentarios de un lugar y no solo un comentario
    #esto lo deberíamos lograr con el serializador SerializerMethodField
class CommentPlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'comment',
            'created',
        )
#una vez hecho este serializador, debemos crear un nuevo serializador para lugares