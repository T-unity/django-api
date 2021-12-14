from django.contrib import admin
# models.pyで作成したHumanクラスをimport
from .models import Human, Tweet

# Humanクラスに対して管理画面から操作できるよう登録
admin.site.register(Human)

class TweetAdmin(admin.ModelAdmin):
  fields = ('name', 'title', 'content', 'created_at', 'updated_at')
  readonly_fields = ('created_at', 'updated_at')

admin.site.register(Tweet, TweetAdmin)
