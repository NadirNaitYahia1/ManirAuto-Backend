from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializers import VoitureSerializer, VoitureDetailSerializer
from .models import Voiture


@api_view(['GET'])
@permission_classes([AllowAny])
def getAnnouncement(request):
    voitures = Voiture.objects.all().select_related('owner')
    serializer = VoitureSerializer(voitures, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def getAnnouncementDetail(request, pk):
    try:
        voiture = Voiture.objects.get(pk=pk)
    except Voiture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = VoitureDetailSerializer(voiture)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addAnnouncement(request):
    if request.method == 'POST':
        serializer = VoitureDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def searchAnnoncement(request):
    # Récupérer les paramètres de recherche depuis la requête
    mark = request.query_params.get('mark', None)
    model = request.query_params.get('model', None)
    annee = request.query_params.get('annee', None)
    prix = request.query_params.get('prix', None)

    # Créer un dictionnaire de filtres basé sur les paramètres de recherche
    filters = {}
    if mark:
        filters['mark__icontains'] = mark
    if model:
        filters['model__icontains'] = model
    if annee:
        filters['annee'] = annee
    if prix:
        filters['prix'] = prix

    # Effectuer la recherche en filtrant les annonces de vente en utilisant les filtres
    voitures = Voiture.objects.filter(**filters)

    # Sérialiser les résultats de la recherche
    serializer = VoitureSerializer(voitures, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def deleteAnnouncement(request, pk):
    try:
        voiture = Voiture.objects.get(pk=pk)
    except Voiture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.user != voiture.owner:
        return Response(status=status.HTTP_403_FORBIDDEN)

    voiture.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def updateAnnouncement(request, pk):
    try:
        voiture = Voiture.objects.get(pk=pk)
    except Voiture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.user != voiture.owner:
        return Response(status=status.HTTP_403_FORBIDDEN)

    serializer = VoitureSerializer(voiture, data=request.data)
    serializer.is_valid(raise_exception=True)

    # Validation supplémentaire
    if serializer.validated_data['annee'] < 1980 or serializer.validated_data['annee'] > 2023:
        raise ValidationError({'annee': ['L\'année doit être comprise entre 1980 et 2023.']})
    if serializer.validated_data['prix'] < 0:
        raise ValidationError({'prix': ['Le prix doit être un nombre positif.']})

    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
    