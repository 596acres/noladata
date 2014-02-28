from django.contrib import admin

from external_data_sync.admin import BaseDataSourceAdmin

from .models import NolaDataSource


class NolaDataSourceAdmin(BaseDataSourceAdmin):
    pass

admin.site.register(NolaDataSource, NolaDataSourceAdmin)
