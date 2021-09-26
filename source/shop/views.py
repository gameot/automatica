from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Shop
from .serializers import ShopInformationSerializer, VisitSerializer


class ShopViewSet(ListModelMixin, GenericViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopInformationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['worker__phone', ]

    @action(
        detail=False,
        methods=('post',),
        url_name='add_visit',
        serializer_class=VisitSerializer
    )
    def add_visit(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
