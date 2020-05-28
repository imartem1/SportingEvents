from django.urls import path, re_path
from .views import index, start_list, start_protocol, result_list,\
    round_results, result_protocol, final_protocol_list, final_protocol

urlpatterns = [
    path('', index, name='index'),
    path('start_list/', start_list, name='start list'),
    re_path(r'^start_list/(\d+)$', start_protocol, name='start_protocol'),
    path('result_list/', result_list, name='result_list'),
    re_path(r'^result_list/(\d+)/(\d+)/(\d+)$', result_protocol, name='result_protocol'),
    re_path(r'^result_list/round_results/(\d+)/(\d+)$', round_results, name='round_results'),
    path('final_list/', final_protocol_list, name='final_protocol_list'),
    re_path(r'^final_protocol/(\d+)$', final_protocol, name='final_protocol'),
]
