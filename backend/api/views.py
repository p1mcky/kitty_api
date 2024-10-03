from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import (
    BreedSerializer, KittySerializer, KittyListSerializer
)
from .filters import KittyFilter
from cats.models import Breed, Kitty, Rating


class BreedViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = [IsAdminOrReadOnly,]
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class KittyViewSet(viewsets.ModelViewSet):
    queryset = Kitty.objects.all()
    serializer_class = KittySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = KittyFilter
    permission_classes = [IsOwnerOrReadOnly,]
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.action in ['list']:
            return KittyListSerializer
        return KittySerializer


class KittyRatingView(viewsets.ViewSet):

    def create(self, request, kitty_id):
        rating = request.data.get('rating')
        if rating < 0 or rating > 5:
            return Response(
                {'error': 'Rating cannot be higher than 5 or lower than 0!'},
                status=status.HTTP_400_BAD_REQUEST
            )
        Rating.objects.update_or_create(
            user=request.user,
            kitty_id=kitty_id, defaults={'rating': rating}
        )
        return Response(
            {'message': 'Rating created or updated successfully'},
            status=status.HTTP_201_CREATED
        )