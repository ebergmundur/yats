# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from yats.models import docs
from yats.forms import DocsForm

def docs_new(request):
    if request.method == 'POST':
        form = DocsForm(request.POST, user=request.user)
        if form.is_valid():
            doc = form.save()
            return HttpResponseRedirect('/docs/view/%s/' % doc.pk)

    else:
        form = DocsForm(user=request.user)
    return render(request, 'docs/new.html', {'layout': 'horizontal', 'form': form})

@login_required
def docs_action(request, mode, docid):
    doc = docs.objects.get(pk=docid)
    if mode == 'view':
        form = DocsForm(user=request.user, instance=doc, view_only=True)
        return render(request, 'docs/view.html', {'layout': 'horizontal', 'form': form, 'doc': doc})

    elif mode == 'edit':
        if request.method == 'POST':
            form = DocsForm(request.POST, user=request.user)
            if form.is_valid():
                doc = form.save()
                return HttpResponseRedirect('/docs/view/%s/' % doc.pk)

        form = DocsForm(user=request.user, instance=doc)
        return render(request, 'docs/edit.html', {'layout': 'horizontal', 'form': form, 'doc': doc})
