#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.http import JsonResponse
from input.models import Movie_list,Content
from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError, ObjectDoesNotExist

def s_all_list(request):
    '''所有电影接口'''
    id = request.GET.get('id', '')

    if id == 'all':
        datas = []
        li = Movie_list.objects.all()
        for i in  li:
            list = {}
            list['id'] = i.id
            list['name'] = i.name
            list['rating_num'] = i.rating_num
            datas.append(list)
        return JsonResponse({'status': 200, 'message': 'success', 'data': datas[:2]})

    if id != 'all':
        return JsonResponse({'status': 10010, 'message': 'id cannot be empty'})





def s_list(request):
    '''查询单条电影接口'''
    id = request.GET.get('id','')

    if id == '':
        return JsonResponse({'status':10021,'message':'id  cannot be empty'})

    if id != '':
        list = {}
        try:
            result = Movie_list.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 10022, 'message': 'nothing'})
        else:
            list['name'] = result.name
            list['rating_num'] = result.rating_num
            return JsonResponse({'status': 200, 'message': 'success', 'data': list})


def short_list(request):
    '''查询短评接口'''
    id = request.GET.get('id','')

    if id == '':
        return JsonResponse({'status':10021,'message':'id  cannot be empty'})

    if id != '':
        list = {}
        try:
            result = Content.objects.get(mid_id=id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 10022, 'message': 'nothing'})
        else:
            list['name'] = result.name
            list['rating_num'] = result.rating_num
            return JsonResponse({'status': 200, 'message': 'success', 'data': list})