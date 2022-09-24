
from django.views.generic.base import TemplateView
from django.contrib import messages


class CalculatorView(TemplateView):
    template_name = "calculator.html"

    def dispatch(self, request, *args, **kwargs):
        return super(CalculatorView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context_data = self.get_context_data()
        return self.render_to_response(context_data)

    def get_context_data(self):

        return {"typeslist": ((1, "Float"), (2, "Hexa"), (3, "Binary")),
                "operatorlist": ((1, "Addition"), (2, "Subtraction"), (3, "Multiplication"))}

    def post(self, request):
        context_data = self.get_context_data()
        post_data = request.POST
        try:
            messages.success(request, "Dc configurations successfully created.")

        except Exception as error:

            messages.error(request, "Failed to create Dc and pst-batch configurations.")

        return self.render_to_response(context_data)