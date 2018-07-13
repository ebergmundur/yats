# -*- coding: utf-8 -*-
from django.conf.urls import  url
from yats.views import root, info, show_board, board_by_id, yatse_api
from yats.tickets import new, action, table, search, reports, workflow
from rpc4django.views import serve_rpc_request

urlpatterns = [
    url(r'^rpc/$',
        view=serve_rpc_request,
        name='tx.tickets.callback'),

   url(r'^$',
        view=root,
        name='view_root'),

   # tickets
   url(r'^tickets/new/$',
        view=new,
        name='new'),

   url(r'^tickets/list/$',
        view=table,
        name='table'),

   url(r'^tickets/search/$',
        view=search,
        name='search'),

   url(r'^tickets/(?P<mode>\w+)/(?P<ticket>\d+)/$',
        view=action,
        name='action'),

   # reports
   url(r'^reports/$',
        view=reports,
        name='reports'),

   # workflow
   url(r'^workflow/$',
        view=workflow,
        name='workflow'),

   # boards
   url(r'^board/(?P<id>\d+)/$',
        view=board_by_id,
        name='board_by_id'),

   url(r'^board/(?P<name>[\w|\W]+)/$',
        view=show_board,
        name='board'),

   # info
   url(r'^info/$',
        view=info,
        name='info'),


   # yatse
   url(r'^yatse/(?P<method>\w+)/$',
        view=yatse_api,
        name='yatse_api'),
]
