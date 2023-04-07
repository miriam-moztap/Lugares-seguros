from rest_framework import serializers
from .models import Place
from apps.comments.models import Comment
from apps.comments.serializers import CommentPlaceListSerializer 


class PlaceSerializers(serializers.ModelSerializer):

    class Meta:

        model = Place
        fields = '__all__'


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
        select_commet = Comment.objects.filter(place__id = obj.id)
        return CommentPlaceListSerializer(select_commet, many=True).data