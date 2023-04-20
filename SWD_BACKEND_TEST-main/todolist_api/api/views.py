from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializers

class TaskList(APIView):
    def get(self,request):
        taskobj=Task.objects.all()
        taskserialize=TaskSerializers(taskobj,many=True)
        return Response(taskserialize.data)
    def post(self,request):
        serializeobj = TaskSerializers(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(serializeobj.data,status=status.HTTP_201_CREATED)
        return Response(serializeobj.errors,status=status.HTTP_400_BAD_REQUEST)

class TaskUpdate(APIView):
    
    def get_object(self,pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,pk):
        taskobj= self.get_object(pk)
        serializeobj = TaskSerializers(taskobj)
        return Response(serializeobj.data)
    
    def put(self,request,pk):
        taskobj = self.get_object(pk)
        taskserialize=TaskSerializers(taskobj,data=request.data)
        if taskserialize.is_valid():
            taskserialize.save()
            return Response(taskserialize.data,status=status.HTTP_200_OK)
        return Response(taskserialize.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        taskobj = self.get_object(pk)
        taskobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    