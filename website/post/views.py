from django.shortcuts import render
from django.views import View


# Create your views here.
class PostPageView(View):
    template_name = "post.html"

    def get(self, request):
        return render(request, self.template_name, context={})
