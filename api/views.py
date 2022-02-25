from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InvestorSerializer
from .models import Investor

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/investor-list/',
		'Detail View':'/investor-detail/<str:pk>/',
		'Create':'/investor-create/',
		'Update':'/investor-update/<str:pk>/',
		'Delete':'/investor-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def investorList(request):
	investors = Investor.objects.all()
	serializer = InvestorSerializer(investors, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def investorDetail(request, pk):
	investor = Investor.objects.get(id=pk)
	serializer = InvestorSerializer(investor, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def investorCreate(request):
	serializer = InvestorSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
		
	return Response(serializer.data)

@api_view(['POST'])
def investorUpdate(request, pk):
	investor = Investor.objects.get(id=pk)
	serializer = InvestorSerializer(instance=investor, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def investorDelete(request, pk):
	task = Investor.objects.get(id=pk)
	task.delete()

	return Response("Data deleted")
