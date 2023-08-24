from PaddleOCR.paddleocr import ocrStart, parse_args
import os
import numpy as np
import cv2

print('')
def draw_det_res(dt_boxes, img):
    if len(dt_boxes) > 0:
        src_im = img
        for box in dt_boxes:
            box = np.array(box)
            box = box.astype(np.int32).reshape((-1, 1, 2))
            cv2.polylines(src_im, [box], True, color=(255, 255, 0), thickness=2)
        cv2.imwrite('./test/1.jpg', src_im)

args = parse_args(mMain=False)
args.use_gpu = False
args.det = True
args.rec = False
args.use_angle_cls = True

text = ocrStart(args, [r'E:\GraduationProject\Django_OCR_backend\upload\idcard20210521142108186743idcard2.png'])
print(text)
img = cv2.imread(r'E:\GraduationProject\Django_OCR_backend\upload\idcard20210521142108186743idcard2.png')
draw_det_res(text[0], img)





# args = parse_args(mMain=False)
# args.use_gpu = False
# args.det = False
# args.rec = True
# args.use_angle_cls = True
#
# text = ocrStart(args, [r'E:\GraduationProject\Django_OCR_backend\upload\20439421_2113843147.jpg'])
# print(text)

