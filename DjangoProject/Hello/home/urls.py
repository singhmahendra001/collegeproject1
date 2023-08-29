from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index , name='home'),
    path("about",views.about , name='about'),
    path("service",views.service , name='service'),
    path("contact",views.contact , name='contact'),
    path("tnontech",views.tnontech, name='tnontech'),
    path("lnontech",views.lnontech, name='lnontech'),
    path("ttech",views.ttech, name='ttech'),
    path("ltech",views.ltech, name='ltech'),
    path("index1",views.index1, name='index1'),
    path("intro",views.intro, name='intro'),
    path("selector",views.selector, name='selector'),
    path("border",views.border, name='border'),
    path("element",views.element, name='element'),
    path("list",views.list, name='list'),
    path("form",views.form, name='form'),
    path("position",views.position, name='position'),
    path("imggallery",views.imggallery, name='imggallery'),
    path("boxmodel",views.boxmodel, name='boxmodel'),
    path("comments",views.comments, name='comments'),
    path("align",views.align, name='align'),
    path("navigation",views.navigation, name='navigation')
]