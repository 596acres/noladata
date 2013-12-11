from django.contrib import admin

from external_data_sync.admin import DataSourceAdmin

from .models import NolaDataSource


class NolaDataSourceAdmin(DataSourceAdmin):
    pass

admin.site.register(NolaDataSource, NolaDataSourceAdmin)
