# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm, ReviewForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def index(request):
    note_list = Note.objects.all()
    random = Note.objects.all().order_by('?')[:1].get()
    return render(request, 'englishnote/index.html', {'note_list':note_list, 'random':random})

def shuffle(request):
    note_list = Note.objects.all()
    random = Note.objects.all().order_by('?')[:1].get()
    random_list = Note.objects.all().order_by('?')[:1]
    return render(request, 'englishnote/index.html', {'random_list':random_list, 'random':random, 'note_list':note_list})

def detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'englishnote/detail.html', {'note': note})

def note_new(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            messages.success(request, '노트가 생성됐습니다.')
            return redirect(reverse('english:index'))
    else:
        form = NoteForm()
    return render(request, 'englishnote/note_form.html', {'form': form})

def note_edit(request, note_pk):
    note = get_object_or_404(Note, pk=note_pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            messages.success(request, '노트가 수정됐습니다.')
            return redirect(reverse('english:detail', args=[note.pk]))
    else:
        form = NoteForm(instance=note)
    return render(request, 'englishnote/note_form.html', {'form': form})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    messages.success(request, '노트가 삭제됐습니다.')
    return redirect(reverse('english:index'))