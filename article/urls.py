from django.urls import path
from rest_framework.routers import DefaultRouter

from article.views import ArticleViewSet, announcement

router = DefaultRouter()  # 创建一个路由器实例
router.register(r'articles', ArticleViewSet)  # 注册视图集
urlpatterns = [
    path('announcement',announcement)
    # 其他 URL 配置
]
# 添加视图集路由
urlpatterns += router.urls
