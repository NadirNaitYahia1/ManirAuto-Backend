from django.urls import path
from . import views
from .views import getAnnouncement


urlpatterns = [
    path('addAnnouncement/', views.addAnnouncement, name='addAnnouncement'),
    #path('', views.getAnnouncement, name='get_announcements'),
    path('announcementDetail/<int:pk>', views.getAnnouncementDetail, name='get_details'),
    path('searchAnnoncement/', views.searchAnnoncement, name='searchAnnoncement'),
    path('deleteAnnouncement/', views.deleteAnnouncement, name='deleteAnnouncement'),
    path('updateAnnouncement/', views.updateAnnouncement, name='updateAnnouncement'),
]
