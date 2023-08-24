# Python and Django-specific imports
import json
import os
from datetime import datetime
from ocr.PaddleOCR.paddleocr import PaddleOCR, parse_args
import re

from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework import filters, generics, status, viewsets
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response

#import needed for working with files
from subprocess import Popen, PIPE, STDOUT

from urllib.parse import urlencode

# Import ocrmypdf, which does the heavy lifting regarding OCR
# Note that ocrmypdf is installed in a virtual environment with Poetry
# import ocrmypdf

import numpy as np
import cv2
import PIL

# Files local to the project
from .serializers import FileSerializer
from .models import Post

from ppocr.utils.logging import get_logger
logger = get_logger()

# 加载识别模型模型
def loadOcrModel(lan=None):
    args = parse_args(mMain=False)
    args.use_gpu = False
    args.det = True
    args.rec = True
    if lan:
        args.lang = lan
    ocr_engine = PaddleOCR(**(args.__dict__))
    return ocr_engine, args
ocr_engine, ocr_args = loadOcrModel()

# 通用识别
class Upload(APIView):

    parser_classes = [MultiPartParser, FormParser]
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        username = data.get('username')
        filetype = data.get('filetype')
        fileslist = request.FILES.getlist('file')
        # print(fileslist)

        # 获取路径
        imglists = []
        for f in fileslist:
            # image_name = data.get('filetype') + '\\' + data.get('filetype') + datetime.now().strftime('%Y%m%d%H%M%S%f') + f.name
            image_name = filetype + datetime.now().strftime('%Y%m%d%H%M%S%f') + f.name
            destination = open(os.path.join(settings.UPLOAD_FILE, image_name), 'wb')
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
            imglists.append(image_name)
        # print(imglists)

        # 识别
        data = []
        for i in range(len(imglists)):
            img = np.array(PIL.Image.open(os.path.join(settings.UPLOAD_FILE, imglists[i])).convert('RGB'))
            logger.info('{}{}{}'.format('*' * 10, imglists[i], '*' * 10))
            result = ocr_engine.ocr(img,
                                    det=ocr_args.det,
                                    rec=ocr_args.rec,
                                    cls=ocr_args.use_angle_cls)
            t = []
            for res in result:
                t.append(res[-1][0])
            text = '&#12288;'.join(t)
            d = {}
            d['id'] = i + 1
            d['file'] = settings.SERVER_HOST + imglists[i].replace('\\', '/')
            d['text'] = text
            data.append(d)
            print(result)

            # 保存数据
            try:
                postdata = Post(
                    username=username,
                    file=imglists[i].replace('\\', '/'),
                    filetype=filetype,
                    text=text,
                )
                postdata.save()
                print(username + ' ' + imglists[i].replace('\\', '/') + ' ' + '保存成功')
            except:
                print(username+' '+imglists[i].replace('\\', '/')+' '+'保存失败')


        print(data)
        # return Response(json.dumps(data,ensure_ascii=False), status=status.HTTP_201_CREATED)
        return Response(data, status=status.HTTP_201_CREATED)

# 不同语种
class Upload_lan(APIView):

    parser_classes = [MultiPartParser, FormParser]
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):

        data = request.data
        print(data)
        username = data.get('username')
        filetype = data.get('filetype')
        fileslist = request.FILES.getlist('file')

        if filetype == 'en':
            ocr_engine_lan, ocr_args_lan = ocr_engine, ocr_args
        else:
            ocr_engine_lan, ocr_args_lan = loadOcrModel(lan=filetype)

        # print(fileslist)
        imglists = []
        for f in fileslist:
            # image_name = data.get('filetype') + '\\' + data.get('filetype') + datetime.now().strftime('%Y%m%d%H%M%S%f') + f.name
            image_name = filetype + datetime.now().strftime('%Y%m%d%H%M%S%f') + f.name
            destination = open(os.path.join(settings.UPLOAD_FILE, image_name), 'wb')
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
            imglists.append(image_name)
        # print(imglists)
        data = []
        for i in range(len(imglists)):
            img = np.array(PIL.Image.open(os.path.join(settings.UPLOAD_FILE, imglists[i])).convert('RGB'))
            logger.info('{}{}{}'.format('*' * 10, imglists[i], '*' * 10))
            result = ocr_engine_lan.ocr(img,
                                    det=ocr_args_lan.det,
                                    rec=ocr_args_lan.rec,
                                    cls=ocr_args_lan.use_angle_cls)
            t = []
            for res in result:
                t.append(res[-1][0])
            text = '&#12288;'.join(t)
            d = {}
            d['id'] = i + 1
            d['file'] = settings.SERVER_HOST + imglists[i].replace('\\', '/')
            d['text'] = text
            data.append(d)
            print(result)

            # 保存数据
            try:
                postdata = Post(
                    username=username,
                    file=imglists[i].replace('\\', '/'),
                    filetype=filetype,
                    text=text
                )
                postdata.save()
                print(username + ' ' + imglists[i].replace('\\', '/') + ' ' + '保存成功')
            except:
                print(username+' '+imglists[i].replace('\\', '/')+' '+'保存失败')

        print(data)
        # return Response(json.dumps(data,ensure_ascii=False), status=status.HTTP_201_CREATED)
        return Response(data, status=status.HTTP_201_CREATED)

# 身份证
class Upload_idcard (APIView):

    parser_classes = [MultiPartParser, FormParser]
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):

        data = request.data
        print(data)
        username = data.get('username')
        filetype = data.get('filetype')
        fileslist = request.FILES.getlist('file')


        # print(fileslist)
        imglists = []
        for f in fileslist:
            # image_name = data.get('filetype') + '\\' + data.get('filetype') + datetime.now().strftime('%Y%m%d%H%M%S%f') + f.name
            image_name = filetype + datetime.now().strftime('%Y%m%d%H%M%S%f') + f.name
            destination = open(os.path.join(settings.UPLOAD_FILE, image_name), 'wb')
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
            imglists.append(image_name)
        print(imglists)
        data = []
        for i in range(len(imglists)):
            img = np.array(PIL.Image.open(os.path.join(settings.UPLOAD_FILE, imglists[i])).convert('RGB'))

            # img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            # retval, img = cv2.threshold(img, 120, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
            # cv2.imwrite('ocr/test/'+ imglists[i], img)

            logger.info('{}{}{}'.format('*' * 10, imglists[i], '*' * 10))
            result = ocr_engine.ocr(img,
                                    det=ocr_args.det,
                                    rec=ocr_args.rec,
                                    cls=ocr_args.use_angle_cls)
            t = []
            for res in result:
                t.append(res[-1][0])
            print(t)
            text = self.print_idcard(t)
            d = {}
            d['id'] = i + 1
            d['file'] = settings.SERVER_HOST + imglists[i].replace('\\', '/')
            d['text'] = text
            data.append(d)
            print(result)

            # 保存数据
            try:
                postdata = Post(
                    username=username,
                    file=imglists[i].replace('\\', '/'),
                    filetype=filetype,
                    text=text
                )
                postdata.save()
                print(username + ' ' + imglists[i].replace('\\', '/') + ' ' + '保存成功')
            except:
                print(username+' '+imglists[i].replace('\\', '/')+' '+'保存失败')

        print(data)
        # return Response(json.dumps(data,ensure_ascii=False), status=status.HTTP_201_CREATED)
        return Response(data, status=status.HTTP_201_CREATED)

    def print_idcard(self, strlist):
        d = {}
        for i in range(len(strlist)):
            if '姓名' in strlist[i]:
                d['xm'] = i
            elif '性别' in strlist[i]:
                d['xb'] = i
            elif '民族' in strlist[i]:
                d['mz'] = i
            elif '出生' in strlist[i]:
                d['cs'] = i
            elif '号码' in strlist[i]:
                d['hm'] =  i
            elif '住址' in strlist[i]:
                d['dz'] =  i
        str = '''
            姓名：{0}<br/>性别：{1}<br/>民族：{2}<br/>出生：{3}<br/>地址：{4}<br/>身份证号码：{5}
        '''.format(
            ''.join(strlist[d['xm']:d['xb']]).replace('姓名', ''),
            ''.join(strlist[d['xb']:d['mz']]).replace('性别', ''),
            ''.join(strlist[d['mz']:d['cs']]).replace('民族', ''),
            ''.join(strlist[d['cs']:d['dz']]).replace('出生', ''),
            ''.join(strlist[d['dz']:d['hm']]).replace('住址', ''),
            ''.join(re.findall("\d+", ''.join(strlist[d['hm']:])))[:18]
        )
        return str

# 车牌识别
class Upload_carcard (APIView):

    parser_classes = [MultiPartParser, FormParser]
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):

        con_list = [
            "皖", "沪", "津", "渝", "冀",
            "晋", "蒙", "辽", "吉", "黑",
            "苏", "浙", "京", "闽", "赣",
            "鲁", "豫", "鄂", "湘", "粤",
            "桂", "琼", "川", "贵", "云",
            "西", "陕", "甘", "青", "宁",
            "新"]
        con_str = ''.join(con_list)

        data = request.data
        print(data)
        username = data.get('username')
        filetype = data.get('filetype')
        fileslist = request.FILES.getlist('file')

        # print(fileslist)
        imglists = []
        for f in fileslist:
            # image_name = data.get('filetype') + '\\' + data.get('filetype') + datetime.now().strftime('%Y%m%d%H%M%S%f') + f.name
            image_name = filetype + datetime.now().strftime('%Y%m%d%H%M%S%f') + f.name
            destination = open(os.path.join(settings.UPLOAD_FILE, image_name), 'wb')
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
            imglists.append(image_name)
        print(imglists)
        data = []
        for i in range(len(imglists)):
            img = np.array(PIL.Image.open(os.path.join(settings.UPLOAD_FILE, imglists[i])).convert('RGB'))

            # img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            # retval, img = cv2.threshold(img, 120, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
            # cv2.imwrite('ocr/test/'+ imglists[i], img)

            logger.info('{}{}{}'.format('*' * 10, imglists[i], '*' * 10))
            result = ocr_engine.ocr(img,
                                    det=ocr_args.det,
                                    rec=ocr_args.rec,
                                    cls=ocr_args.use_angle_cls)
            t = []
            for res in result:
                t.append(res[-1][0])
            print(t)
            text = '<br/>'.join([i for i in t if i.strip()[0] in con_str and len(i)>6 and len(i)<9])
            d = {}
            d['id'] = i + 1
            d['file'] = settings.SERVER_HOST + imglists[i].replace('\\', '/')
            d['text'] = text
            data.append(d)
            print(result)

            # 保存数据
            try:
                postdata = Post(
                    username=username,
                    file=imglists[i].replace('\\', '/'),
                    filetype=filetype,
                    text=text
                )
                postdata.save()
                print(username + ' ' + imglists[i].replace('\\', '/') + ' ' + '保存成功')
            except:
                print(username+' '+imglists[i].replace('\\', '/')+' '+'保存失败')

        print(data)
        # return Response(json.dumps(data,ensure_ascii=False), status=status.HTTP_201_CREATED)
        return Response(data, status=status.HTTP_201_CREATED)


def getLan(param):
    if param == 'img':
        return '通用'
    if param == 'en':
        return '英语'
    if param == 'french':
        return '法语'
    if param == 'german':
        return '德语'
    if param == 'japan':
        return '日语'
    if param == 'idcard':
        return '身份证'


# 识别历史
class Historydata(APIView):

    parser_classes = [MultiPartParser, FormParser]
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')

        username_data = Post.objects.filter(username=username).values_list('username', 'filetype', 'file', 'text', 'uploaded')
        print(username_data)
        data = []
        for i in range(len(username_data)):
            d = {}
            d['id'] = i+1
            # d['username'] = username_data[i][0]
            d['filetype'] = getLan(username_data[i][1])
            d['file'] = settings.SERVER_HOST + username_data[i][2]
            d['text'] = username_data[i][3]
            d['date'] = username_data[i][4].strftime('%Y-%m-%d %H:%M:%S')
            data.append(d)
        return Response(data, status=status.HTTP_201_CREATED)





# class PostList(generics.ListAPIView):
#     # permission_classes = [IsAuthenticated]
#     serializer_class = FileSerializer
#     queryset = Post.objects.all()
#
#
# # The view showing us the details of individual posts
# class PostDetail(generics.RetrieveAPIView):
#
#     serializer_class = FileSerializer
#
#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)
#
# # This will allow us to search
# class PostListDetailfilter(generics.ListAPIView):
#
#     queryset = Post.objects.all()
#     serializer_class = FileSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['^slug']
#
# # Post Admin
#
# class CreatePost(generics.CreateAPIView):
#     # permission_classes = [IsAuthenticated]
#     parser_classes = [MultiPartParser, FormParser]
#     serializer_class = FileSerializer
#
#     def post(self, request, *args, **kwargs):
#         print(request.data)
#
#         posts_serializer = FileSerializer(data=request.data)
#
#         if posts_serializer.is_valid():
#
#             # The below removes the necessity to hard-code the path to the input file.
#             uploaded = posts_serializer.save()
#
#             # process = Popen(['ocrmypdf', uploaded, 'output.pdf'])
#
#             _, img = ctpn.predict(self.filename)
#
#             _, texts = textdetectionApp.detect(self.filename, True)
#             text = '\n'.join(texts)
#
#             return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
#
#         else:
#             print('error', posts_serializer.errors)
#             return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
# class AdminPostDetail(generics.RetrieveAPIView):
#     # permission_classes = [IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = FileSerializer
#
# class EditPost(generics.UpdateAPIView):
#     # permission_classes = [IsAuthenticated]
#     serializer_class = FileSerializer
#     queryset = Post.objects.all()
#
# class DeletePost(generics.RetrieveDestroyAPIView):
#     # permission_classes = [IsAuthenticated]
#     serializer_class = FileSerializer
#     queryset = Post.objects.all()
