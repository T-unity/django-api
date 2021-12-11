from django.contrib import admin
# models.pyで作成したHumanクラスをimport
from .models import Human

# Humanクラスに対して管理画面から操作できるよう登録
admin.site.register(Human)
