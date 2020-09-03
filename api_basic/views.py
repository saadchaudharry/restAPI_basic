from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Artical
from .serilizer import Articlr_serlier
from rest_framework.decorators import api_view
from rest_framework.views import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,CreateAPIView,ListAPIView
from rest_framework import mixins

class Articalcret(GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin):

    serializer_class = Articlr_serlier
    queryset = Artical.objects.all()
    lookup_field = 'id'

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.post(request)

    def put(self,request,id=None):
        self.update(request,id)

    def delete(self,request,id=None):
        self.destroy(request,id)


# class Artical_id(GenericAPIView,mixins.UpdateModelMixin,)


class Articvalapi(APIView):

    def get(self,request):
        article = Artical.objects.all()
        serializer = Articlr_serlier(article, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = Articlr_serlier(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






# Create your views here.
@api_view(["GET","POST"])
def basic_view(request):
    if request.method == "GET":
        article =Artical.objects.all()
        serializer=Articlr_serlier(article,many=True)
        return Response(serializer.data)

    elif request.method =="POST":
        serializer=Articlr_serlier(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET","PUT","DELETE"])
def artical_psk(request,pk):
    artical =Artical.objects.all()
    artt=get_object_or_404(artical ,pk=pk)

    if request.method == "GET":
        serializer =Articlr_serlier(artt)
        return Response(serializer.data)

    elif request.method == "PUT":
        # data=JSONParser().parse(request)
        serializer=Articlr_serlier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        artt.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)
