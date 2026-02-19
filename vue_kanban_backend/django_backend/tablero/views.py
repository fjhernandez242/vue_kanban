from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import TableroSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import tablero_model
from django.utils import timezone

from .forms import TableroForm

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def trabajos(request):
    # se obienen todos los trabajos
    get_trabajos = tablero_model.objects.all()
    # Se envian a serializar el objeto
    serializer = TableroSerializer(instance=get_trabajos, many=True)
    return Response({ "trabajos": serializer.data }, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getTrabajoById(request):
    data = request.data
    trabajo = tablero_model.objects.get(id=data['id'])
    serializer =  TableroSerializer(instance=trabajo)
    return Response({ "trabajo": serializer.data }, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def agregar_trabajo(request):

    form = TableroForm(request.POST, request.FILES)
    if form.is_valid():
        exist_trabajo = tablero_model.objects.filter(guia=form.cleaned_data['guia'])
        if exist_trabajo.exists():
            return Response({ "error": "Ya existe un trabajo con esta guia" })
        try:
            tablero_model.objects.create(
                    guia = form.cleaned_data['guia'],
                    recibio = form.cleaned_data['recibio'],
                    lista = form.cleaned_data['lista'],
                    desc = form.cleaned_data['desc'],
                    cliente = form.cleaned_data['cliente'],
                    imagen = form.cleaned_data['imagen'],
                    fecha_recepcion = timezone.now()
                )
        except:
            return Response({ "error": "Algo salio mal" })

        serializador = TableroSerializer(form, many=True)
        return Response({ "data": serializador.data }, status=status.HTTP_200_OK)
    else:
        return Response({ "error": "Formulario invalido" })

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def cambiar_posicion(request):
    estados = {
        1: 'Evaluación',
        2: 'Espera',
        3: 'Reparación',
        4: 'Entregado',
    }
    data = request.data
    try:
        # Intenta obtener el objeto. Si no existe, salta al 'except'
        exist_trabajo = tablero_model.objects.get(guia=data['guia'])
        # Si se encontró, actualiza y guarda
        exist_trabajo.lista = data.get('posicion')
        exist_trabajo.estado = estados[data.get('posicion')]
        exist_trabajo.save()
        return Response({ "guia": data['guia'], "mensaje": "Posición actualizada" }, status=status.HTTP_200_OK)

    except tablero_model.DoesNotExist:
        # Si el objeto NO existe, retorna la respuesta de error.
        return Response({ "error": "No existe el trabajo con esa guía" }, status=status.HTTP_404_NOT_FOUND)
    except KeyError:
        # Manejar si 'guia' o 'posicion' no están en la data
        return Response({ "error": "Faltan datos requeridos (guia o posicion)" }, status=status.HTTP_400_BAD_REQUEST)