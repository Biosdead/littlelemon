from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import booking,menu,User
from .serializers import bookingSerializer,MenuItemSerializer,UserSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,api_view

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class bookingview(APIView):
    def get(self,request):
        items = booking.objects.all()
        serializer = bookingSerializer(items,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = bookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data" : serializer.data})

class menuview(APIView):
    def get(self,request):
        items = menu.objects.all()
        serializer = MenuItemSerializer(items,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data" : serializer.data})

class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = bookingSerializer
    # ⬇️  protege TODAS as ações (list, retrieve, create, etc.)
    permission_classes = [IsAuthenticated]

@permission_classes([IsAuthenticated])
class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated]


@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message":"This view is protected"})