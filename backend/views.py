from .models import Wiki
from .serializer import WikiSerializer
from rest_framework import generics

# Create your views here.

class WikiListView(generics.ListAPIView):
    queryset = Wiki.objects.all().order_by('-created_on')
    serializer_class = WikiSerializer
