from rest_framework import serializers
from .models import Place
from apps.comments.models import Comment
from apps.comments.serializers import CommentPlaceListSerializer


class PlaceSerializers(serializers.ModelSerializer):

    class Meta:

        model = Place
        fields = '__all__'

        #esto es parte del video9, y vamos a crear un serializador diferente para hacer que, cuando se llame un lugar específico, se desplieguen también todos sus comentarios

class PlaceListCommentSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField() #este es un atributo declarado para poder traer ese atributo de comment a nuestro place, el nombre debe ser exacto

    class Meta:
        model = Place
        fields = (
            'id',
            'name',
            'comment',
        ) #este campo de fields se refiere a los datos del comentario que se van a mostrar cuando se llame un lugar

    def get_comment(self, obj):
        selected_comment = Comment.objects.filter(place__id = obj.id)
        return CommentPlaceListSerializer(selected_comment, many=True).data