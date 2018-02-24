from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


def handler500(request):
    """500 error handler which includes ``request`` in the context.

    Templates: `500.html`
    Context: None
    """

    context = {'request': request}
    template_name = '500.html'  # You need to create a 500.html template.
    return TemplateResponse(request, template_name, context, status=500)
