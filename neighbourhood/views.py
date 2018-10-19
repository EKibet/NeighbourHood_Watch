from django.shortcuts import render

# Create your views here.
# @login_required(login_url='/login/')
# def search_results(request):
#     if 'searchItem' in request.GET and request.GET["searchItem"]:
#         search_term = request.GET.get("searchItem")
#         searched_project = PostedSite.search_by_site(search_term)
#         # user = User.objects.get(username=searched_user)
#         # user_images = Profile.objects.get(user=searched_user)
#         message = f"{search_term}"
#         context = {
#             'message': message,
#             'projects': searched_project
#         }
#         return render(request, 'awards/search.html', context)

#     else:
#         messages.success(request, f"You haven't searched for any term")

#         return render(request, 'awards/search.html',{"message":message})
