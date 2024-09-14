from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
urlpatterns = [
    path('my_final/', views.my_final, name='my_final'),
    path('', views.welcome, name='home'),
    path('register/', views.registerView, name='register'),
    path('patient/', views.patientView, name='patient'),
    path('patpage/', views.patient_dashboard, name='patpage'),
    path('login/', views.loginView, name='login'),
    path('donpage/', views.donor_dashboard, name='donpage'),
    path('available/', views.available, name="available"),
    path('profile/', views.profileView, name='profile'),
    path('profile/changepassword/', views.changePasswordView, name='changepassword'),
    path('request/', views.createReqView, name="createreq"),
    path('allrequest/', views.allReqView, name='allrequest'),
    path('donor/<int:id>/', views.detailView, name="details"),
    path('group/<int:id>/', views.groupView, name='group'),
    path('profile/update/', views.editProfileView, name='updateprofile'),
    path('editrequest/', views.editRequestView, name="editrequest"),
    path('getrequest/', views.getRequestView, name="getrequest"),
    path('deleterequest/<int:pin>/', views.deleteRequestView, name="deleterequest"),
    path('logout/', views.logoutView, name='logout'),
    path('status/', views.statusView, name='status'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
