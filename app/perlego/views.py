from django.shortcuts import render
from .parser import parse_xml
import country_converter as cc
from django.core.files.storage import FileSystemStorage
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, mixins
from django.views import View


    
class CreateBookViewSet(View):
    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES['document']
        title, raw_data = parse_xml(uploaded_file)
        countries = cc.convert(names=raw_data, to='name_short')
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        book_instances = Book.objects.filter(title=title, countries=countries)
        _, book_instance = Book.objects.get_or_create(title=title, countries=countries)        
        return render(request, 'perlego/upload.html')
    
    def get(self, request):
        return render(request, 'perlego/upload.html')
        

    
class BookViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_queryset(self):
        return self.queryset
    

