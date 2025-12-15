from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Conversation
from .serializers import ConversationListSerializer

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def conversations_list(request):
    # Get conversations where the current user is a participant
    conversations = request.user.conversations.all()
    serializer = ConversationListSerializer(conversations, many=True)
    return JsonResponse(serializer.data, safe=False)