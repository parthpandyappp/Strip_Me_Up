from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import stripurl
from .serializers import StripUrlSerializer


class StripURLCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of URLs or create new
    """
    serializer_class = StripUrlSerializer
    queryset = stripurl.objects.all()


class StripURLDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete any URL
    """
    serializer_class = StripUrlSerializer
    queryset = stripurl.objects.all()

    