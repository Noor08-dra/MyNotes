from gc import get_objects
from django.shortcuts import render,redirect
from . import forms
from . import models
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView,FormMixin
from django.urls import reverse_lazy,reverse


def home(request):
      return render(request,"home.html")

class NoteCreateView(CreateView):
     model=models.Notes
     template_name="Notes/note_form.html"
     form_class=forms.NotesForm
     success_url=reverse_lazy("notes_list")

class NoteListView(ListView):
     model=models.Notes
     template_name="account/list.html"
     context_object_name="notes"
     ordering=["-created_at"]


class NoteDetailView(DetailView,FormMixin):
     model=models.Notes
     template_name="Notes/detail_page.html"
     context_object_name="note"
     form_class=forms.ReplyForm
     
     def get_success_url(self):
             success_url=reverse_lazy("detail_page",kwargs={"pk":self.object.pk})        
             return success_url
     def post(self,request,*args,**kwargs):
          self.object=self.get_object()
          form=self.get_form()
          if form.is_valid():
              return self.form_valid(form)
          else: 
              return self.form_invalid(form)
     
     def form_valid(self,form):
          form.instance.note=self.object
          reply=form.save()
          return super().form_valid(form)
     
     def get_context_data(self,*args,**kwargs):
              context = super().get_context_data(**kwargs)
              context["replies"]= self.object.replies.all().order_by("-created_at")
              return context
          

class NoteEditView(UpdateView):
     model=models.Notes     
     form_class=forms.NotesForm
     template_name="Notes/note_form.html"
     context_object_name="note"
     success_url=reverse_lazy("notes_list")

class NoteDeleteView(DeleteView):
     model=models.Notes
     template_name="Notes/note_delete.html"
     context_object_name="note"
     success_url=reverse_lazy("notes_list")

class ReplyEditView(UpdateView):
      model=models.Reply
      context_object_name="reply"
      template_name="Notes/reply_edit.html"
      form_class=forms.ReplyForm

      def get_success_url(self):
          return reverse_lazy("detail_page",kwargs={'pk': self.object.note.pk})
      
class ReplyDeleteView(DeleteView):
     model=models.Reply
     context_object_name="reply"
     
     def get_success_url(self):
          return reverse_lazy("detail_page",kwargs={'pk': self.object.note.pk})