from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets, generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.filters import AdFilter
from ads.models import Ad
from ads.permissions import IsAdmin, IsOwner
from ads.serializers import AdDetailSerializer, AdSerializer

from skymarket.ads.models import Comment


class AdPagination(pagination.PageNumberPagination):
    """Пагинация"""

    page_size = 4
    page_size_query_param = "page_size"
    max_page_size = 10


class AdViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели объявления"""

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdFilter

    def get_serializer_class(self):
        """Выбор сериалайзера"""
        if self.action in ["retrieve", "create", "update", "partial_update", "destroy"]:
            return AdDetailSerializer
        return AdSerializer

    def get_permissions(self):
        """Выбор прав доступа"""
        if self.action == "list":
            permission_classes = [AllowAny]
        elif self.action in ["retrieve", "create"]:
            permission_classes = [IsAuthenticated]
        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """Сохранение автора объявления"""
        ad = serializer.save()
        ad.author = self.request.user
        ad.save()


class AdsListApiView(generics.ListAPIView):
    """Просмотр списка объявлений"""
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Вывод только объявлений текущего пользователя"""
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели отзыва"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
