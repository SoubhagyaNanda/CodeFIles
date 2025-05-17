from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from students.models import Students
from employee.models import Employees
from .serializers import studentsSerializers, employeeSerializers, CommentSerializers, BlogSrializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import Http404
from rest_framework import mixins, generics, viewsets
from django.shortcuts import get_object_or_404
from blog.models import blogModels, blogComment
# from blog.serializers import CommentSerializers, BlogSerializers
from .paginations import CustomPagination
from employee.filters import EmployeeFilter
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.

#Get and Post view
@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method == 'GET':
        students = Students.objects.all()
        serializer= studentsSerializers(students, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    elif request.method=='POST':
        serializer = studentsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Single data view
@api_view(['GET','PUT','DELETE'])
def studentdetailView(request,pk):
    try:
        student= Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer = studentsSerializers(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer = studentsSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class employeeView(APIView):
#     def get(self, request):
#         employee = Employees.objects.all()
#         serializer= employeeSerializers(employee, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer= employeeSerializers(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class employeeDetails(APIView):
#     def get_object(self,pk):
#         try:
#             return Employees.objects.get(pk=pk)
#         except Employees.DoesNotExist:
#             raise Http404
#     def get(self,request,pk):
#         employee = self.get_object(pk)
#         serializer= employeeSerializers(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def put(self,request,pk):
#         employee = self.get_object(pk)
#         serializer = employeeSerializers(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request, pk):
#         employee= self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_404_NOT_FOUND)


# Mixins
class employeemixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employees.objects.all()
    serializer_class = employeeSerializers

    def get(self, request):
        return self.list(request)

    def post(self,request):
        return self.create(request)
# Mixins
class employeemixinsdetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employees.objects.all()
    serializer_class = employeeSerializers

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


# Generics
'''class GenericView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = employeeSerializers'''

class GenericView(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = employeeSerializers

'''class GenericDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = employeeSerializers
    lookup_field= 'pk' '''

class GenericDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = employeeSerializers
    lookup_field = 'pk'

# viewsets
'''class employeeview(viewsets.ViewSet):
    def list(self, request):
        queryset = Employees.objects.all()
        serializer_class = employeeSerializers(queryset, many=True)
        return Response(serializer_class.data)

    def create(self, request):
        serializer= employeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def retrieve(self, request, pk= None):
        queryset = get_object_or_404(Employees, pk=pk)
        serializer= employeeSerializers(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = get_object_or_404(Employees, pk=pk)
        serializer = employeeSerializers(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def __delete__(self, request, pk=None):
        queryset = get_object_or_404(Employees, pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''


# Model viewset
class employeeview(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = employeeSerializers
    pagination_class = CustomPagination
    filterset_class = EmployeeFilter      # Custom filter
    # filterset_fields = ['emp_desi']    # Global Filter

# Nested Serialize
class blogView(generics.ListCreateAPIView):
    queryset = blogModels.objects.all()
    serializer_class = BlogSrializers
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields= ['^blog_title','blog_body']
    ordering_fields= ['id', 'blog_title']

class commentView(generics.ListCreateAPIView):
    queryset = blogComment.objects.all()
    serializer_class = CommentSerializers

class blogdetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = blogModels.objects.all()
    serializer_class = BlogSrializers
    lookup_field = 'pk'

class commentdetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = blogComment.objects.all()
    serializer_class = CommentSerializers
    lookup_field = 'pk'