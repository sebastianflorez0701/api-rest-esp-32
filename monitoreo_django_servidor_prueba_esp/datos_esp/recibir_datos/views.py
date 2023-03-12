
from django.http import  JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from recibir_datos.serializers import VoltajeCorrienteSerializer
from recibir_datos.models import VoltajeCorriente

@csrf_exempt
def datos_list(request):
    """
    List all code data, or create a new recibir_datos.
    """
    if request.method == 'GET':
        datos = VoltajeCorriente.objects.all()
        serializer = VoltajeCorrienteSerializer(datos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VoltajeCorrienteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)