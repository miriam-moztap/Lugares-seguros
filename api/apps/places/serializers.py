from rest_framework import serializers
from .models import Place
from apps.comments.models import Comment
from apps.comments.serializers import CommentPlaceListSerializer


class PlaceSerializers(serializers.ModelSerializer):

    class Meta:

        model = Place
        fields = '__all__'

<<<<<<< HEAD
class PlaceListCommentSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()
    class Meta:
        models = Place
        fields = (
            'id',
            'name',
            'comment',
            
        )
    
    def get_comment(self, obj):
        selected_comment = Comment.objects.filter(place_id = object.id)
        return CommentPlaceListSerializer(selected_comment, many = True).data

=======
class PlacelistCommentSerializer(serializers.ModelSerializer):

    comment = serializers.SerializerMethodField()

    class Meta:

        model = Place
        fields = (
            'id',
            'name',
            'comment'
        )
    
    def get_comment(self, obj):
        selected_comment = Comment.objects.filter(place__id = obj.id)
        return CommentPlaceListSerializer(selected_comment, many=True).data
>>>>>>> 5357af978d8fc2f4f806b0e7f30ab53a00305135
