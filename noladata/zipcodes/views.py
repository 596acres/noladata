from django.http import Http404

from inplace.boundaries.views import BoundaryDetailView

from .models import ZipCode


class ZipCodeDetailView(BoundaryDetailView):
    model = ZipCode

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        try:
            return queryset.get(label=self.kwargs.get('label', None))
        except ZipCode.DoesNotExist:
            raise Http404
