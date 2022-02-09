from testapp1.models import Employee
from testapp1.serializers import EmployeeSerializer
from rest_framework.response import Response
import io
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def employee_detail(request):
    if request.method == 'GET':
        jdata = request.body
        bobj = io.BytesIO(jdata)
        data = JSONParser().parse(bobj)
        id = data.get('id')
        if id is not None:
            try:
                emp = Employee.objects.get(id=id)
            except Employee.DoesNotExist:
                return Response({'msg':'record not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data, status=status.HTTP_200_OK)
        emp_qs = Employee.objects.all()
        serializer = EmployeeSerializer(emp_qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        jdata = request.body
        bobj = io.BytesIO(jdata)
        data = JSONParser().parse(bobj)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response({'msg':'plz send the valid data'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        jdata = request.body
        bobj = io.BytesIO(jdata)
        data = JSONParser().parse(bobj)
        id = data.get("id")
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            return Response({'msg':'record not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(emp, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'resource updated successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response({'msg':'plz send the valid data'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        jdata = request.body
        bobj = io.BytesIO(jdata)
        data = JSONParser().parse(bobj)
        id = data.get("id")
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            return Response({'msg':'record not found'}, status=status.HTTP_404_NOT_FOUND)
        emp.delete()
        return Response({'msg':'record deleted'}, status=status.HTTP_204_NO_CONTENT)

