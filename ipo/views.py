from django.shortcuts import render
from rest_framework import generics
from .models import IPO
from .serializers import IPOSerializer

# API Views
class IPOListAPIView(generics.ListAPIView):
    queryset = IPO.objects.all().order_by('-open_date')
    serializer_class = IPOSerializer

class IPODetailAPIView(generics.RetrieveAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
    lookup_field = 'pk'

# Template Views
def ipo_list_view(request):
    return render(request, 'ipo/index.html')

def ipo_detail_page_view(request, pk: int):
    # Template fetches data via JS
    return render(request, 'ipo/ipo_detail.html', {'pk': pk})
