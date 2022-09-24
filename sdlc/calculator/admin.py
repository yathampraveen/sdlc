from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse



from .models import Calculator


@admin.register(Calculator)
class CalculatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def get_search_url(self):
        """
        Return the custom search url for this admin page
        """
        return reverse("calculator-view")

    def changelist_view(self, request, extra_context=None):

        search_url = self.get_search_url()

        if not search_url:
            return super(CalculatorAdmin, self).changelist_view(
                request, extra_context=extra_context
            )

        get_params = request.GET.keys()
        if not get_params:
            return HttpResponseRedirect("%s" % search_url)

        return super(CalculatorAdmin, self).changelist_view(
            request, extra_context=extra_context
        )


