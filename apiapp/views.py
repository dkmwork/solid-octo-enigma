from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student

@api_view(['GET','POST'])
def student_operations(request):
    if request.method == "GET":
        return Response({'Message':"Hi Divya"})
    elif request.method == "POST":
        studentscr= StudentSerializer(data=request.data)
        if studentscr.is_valid():
            studentscr.save()
            return Response({'Message':"Data Saved"})
        else:
            return Response({'Message':"Data Not Saved"})
@api_view(['GET','PUT'])
def update_student(request,id):
    if request.method =="GET":
        studentobj=Student.objects.get(s_id=id)
        context={'request': request}
        studentscr=StudentSerializer(studentobj)
        print(studentscr)
        return Response({"Messgae":studentscr.data})
    elif request.method =="PUT":
        studentobj=Student.objects.get(s_id=id)
        studentscr=StudentSerializer(data=request.data, instance=studentobj)
        if studentscr.is_valid():
            studentscr.save()
            return Response({"Message":studentscr.data})
        else:
            return Response({status:status.HTTP_404_NOT_FOUND})

        

# Create your views here.
