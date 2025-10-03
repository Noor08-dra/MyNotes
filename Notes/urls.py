from django.urls import path
from . import views


urlpatterns = [
    path("",views.home,name="home"),
    path('notes/', views.NoteListView.as_view(),name="notes_list"),
    path('notes/add/', views.NoteCreateView.as_view(),name="note_form_create"),
    path("notes/<int:pk>/", views.NoteDetailView.as_view(),name="detail_page"),
    path('notes/<int:pk>/edit/', views.NoteEditView.as_view(),name="note_form_edit"),
    path('notes/<int:pk>/delete/', views.NoteDeleteView.as_view(),name="note_delete"),
    path("replies/<int:pk>/edit/",views.ReplyEditView.as_view(),name="edit_reply"),
    path("replies/<int:pk>/delete/",views.ReplyDeleteView.as_view(),name="delete_reply"),
]

