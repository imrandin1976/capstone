from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import bookingSerializer, menuSerializer
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializers import menuSerializer

def index(request):
    return render(request, 'index.html', {})

class bookingView(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many = True)
        return Response(serializer.data)
    
class menuView(APIView):
    def post(self, request):
        serializer = menuSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data": serializer.data})

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    def get(self, request):
        return Response({"data": request.data})
    

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class bookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})
    

