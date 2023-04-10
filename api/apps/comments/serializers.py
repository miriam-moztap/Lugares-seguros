from rest_framework import serializers
from .models import Comment


class CommentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Comment
        #fields = '__all__'
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
<<<<<<< HEAD
class CommentPlaceListSerializer(serializers.ModelSerializer):
=======

class CommentPlaceListSerializer(serializers.ModelSerializer):

>>>>>>> 5357af978d8fc2f4f806b0e7f30ab53a00305135
    class Meta:
        model = Comment
        fields = (
            'id',
            'comment',
<<<<<<< HEAD
            'created'
=======
            'created',
>>>>>>> 5357af978d8fc2f4f806b0e7f30ab53a00305135
        )