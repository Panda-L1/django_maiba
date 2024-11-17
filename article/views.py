from rest_framework.serializers import ModelSerializer

from accounts.models import CustomUser
from rest_framework.response import Response
from rest_framework.decorators import api_view

from utils.result import Result
class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']  # 指定序列化字段

# Create your views here.
@api_view(['GET'])
def show_view(request):
    users = CustomUser.objects.all()
    users_serialized = CustomUserSerializer(users, many=True).data
    result = Result(200, 'success', users_serialized).to_dict()
    return Response(result,status=200)
