# from django.http import HttpResponse
# from django.template import loader

from amazoom.models import *  # import all models
from amazoom.owner import OwnerListView, OwnerDetailView, OwnerDeleteView
from django.views import View
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from amazoom.forms import CreateForm, CommentForm


class IndexView(OwnerListView):
    # output = "hello"
    # return HttpResponse(output)

    model = Listing

    template = 'amazoom/index.html'

    def get(self, request):
        ad_list = Listing.objects.all()
        ctx = {'ad_list': ad_list}
        return render(request=request, template_name=self.template, context=ctx)
class ItemAdd(LoginRequiredMixin, View):
    template_name = 'amazoom/add_item.html'
    success_url = reverse_lazy('ads:index')

    def get(self, request, pk):
        pic = get_object_or_404(Product, id=pk, owner=self.request.user)
        form = CreateForm(instance=pic)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        pic = get_object_or_404(Product, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        pic = form.save(commit=False)
        pic.save()

        return redirect(self.success_url)

    fields = ['title', 'text', 'price']

def user_register(request):
    template = 'amazoom/signup.html'

    return render(request=request, template_name=template)


def user_signin(request):
    template = 'amazoom/signin.html'

    return render(request=request, template_name=template)

# def index(request):
#     # output = "hello"
#     # return HttpResponse(output)
#     template = 'amazoom/index.html'
#
#     return render(request=request, template_name=template)
#
#
# def user_register(request):
#     template = 'amazoom/signup.html'
#
#     return render(request=request, template_name=template)
#
#
# def user_signin(request):
#     template = 'amazoom/signin.html'
#
#     return render(request=request, template_name=template)

#

# def edit_product():
#     template = ""
#
# def delete_product():
#     template = ""
#
# def ():
#     template = ""
#
# def ():
#     template = ""
