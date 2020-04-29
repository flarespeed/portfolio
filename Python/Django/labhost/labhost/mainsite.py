from django.shortcuts import render
from django.http import HttpResponse

url_list={'lab01': '/polls/', 'lab02': '/contacts/', 'lab03': '/redir/', 'lab04': '/library/', 'accounts': '/accounts/', 'vue.js integration lab': '/todos/'}

def index(request):
    html_list = '<h3>Labhost<h3><ul>'
    for url in url_list:
        html_list += '<li><a href="' + url_list[url] + '">' + url + '</a></li>'
    html_list += '</ul>'
    return HttpResponse(html_list)
