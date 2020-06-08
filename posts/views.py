from django.shortcuts import render


from django.views.generic import ListView

from .models import Post

# Create your views here.

#umesto da na html referenciramo object_list, što je generičko ime za objekat koji ListView vraća
#upotrebićemo context_object_name da damo neko deskriptivnije ime da ga referenciramo na html strani

class HomePageView(ListView):

	model = Post
	template_name = "home.html"
	context_object_name = "all_posts_list"