from django.urls import path
from .views import MainView, PostDetailView, SignUpView, SignInView, sign_out, SuccessView, FeedBackView, SearchResultsView, TagView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('blog/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', sign_out, name='signout',),
    path('contact/', FeedBackView.as_view(), name='contact'),
    path('contact/success/', SuccessView.as_view(), name='success'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('tag/<slug:slug>/', TagView.as_view(), name="tag"),
]

# from django.urls import path
# # from .views import MainView
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]