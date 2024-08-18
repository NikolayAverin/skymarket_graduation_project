from rest_framework import serializers

from ads.models import Ad


class CommentSerializer(serializers.ModelSerializer):
    """Сериалайзер для комментария"""

    pass


class AdSerializer(serializers.ModelSerializer):
    """Сериалайзер для объявления"""

    class Meta:
        model = Ad
        fields = (
            "id",
            "title",
            "price",
            "description",
        )


class AdDetailSerializer(serializers.ModelSerializer):
    """Сериалайзер для детального представления объявления"""

    author_first_name = serializers.CharField(
        source="author.first_name", read_only=True
    )
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)

    class Meta:
        model = Ad
        fields = "__all__"
