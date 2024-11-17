from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from article.models import Article


class ArticleSerializer(ModelSerializer):
    user_id = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
            model = Article
            fields = ['article_id', 'title', 'content', 'user_id', 'user_name', 'create_time', 'remark_num', 'click_num']

    def get_user_id(self, obj):
        return obj.user.id  # 从外键字段获取作者ID

    def get_user_name(self, obj):
        return obj.user.username  # 从外键字段获取作者姓名