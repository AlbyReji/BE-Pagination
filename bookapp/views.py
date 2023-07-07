from .models import Books
from .serializers import BookSerializer
from rest_framework import generics
from .pagination import NumberPagination

class BookCreateList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    pagination_class = NumberPagination


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

