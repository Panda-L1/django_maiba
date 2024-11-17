from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_redis import get_redis_connection
from rest_framework.viewsets import ModelViewSet
from article.models import Article
from serializers.articleSerializer import ArticleSerializer
from utils.result import Result


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    def list(self, request, *args, **kwargs):
        # 获取 'limit' 参数，默认为 10
        limit = request.query_params.get('limit', 2)
        # 使用 `.all()` 查询数据并限制数量
        queryset = self.get_queryset()[:int(limit)]  # 截取前 limit 条数据
        print(queryset.query)
        # 使用序列化器序列化数据
        serializer = self.get_serializer(queryset, many=True)
        # # 获取所有文章
        # response = super().list(request, *args, **kwargs)

        # 使用 Result 封装返回格式
        result = Result(200, 'Success', serializer.data).to_dict()
        print(result)
        return Response(result)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        # 使用 Result 封装返回格式
        result = Result(201, 'Article created successfully', response.data).to_dict()
        print(result)
        return Response(result, status=201)

from rest_framework.response import Response
from redis import Redis
@api_view(['get'])
def announcement(request):
    # 确保 Redis 连接正确
    conn = get_redis_connection()

    # 获取 Redis 中的 'announcement' 键的值
    data = conn.get('announcement')

    if data is None:
        data = "Default announcement message"  # 如果没有数据，则使用默认值
    else:
        data = data.decode('utf-8')  # 解码为 UTF-8 字符串

    # 确保 to_dict 返回的是字典
    result = Result(200, 'Success', data).to_dict()
    print(result)  # 打印查看 result 的内容，确保是字典

    return Response(result, status=200)
