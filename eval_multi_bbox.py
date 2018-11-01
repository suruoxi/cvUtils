#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ************************************************************************ 
# * 
# * @file: evaluate_logo.py 
# * @author: futian.zp 
# * @date: 2018-01-18 17:40 
# * @version 1.0  
# * @description: Python Script 
# * @Copyright (c)  all right reserved 
# * 
#************************************************************************* 

def cal_iou(val1, val2):
    """
    cal crop IOU
    :param val1: [x11,y11,x12,y12]
    :param val2: [x21,y21,x22,y22]
    :return type: float
    """


    x11, y11, x12, y12 = val1
    x21, y21, x22, y22 = val2

    leftX = max(x11, x21)
    topY = max(y11, y21)
    rightX = min(x12, x22)
    bottomY = min(y12, y22)

    if rightX < leftX or bottomY < topY: return 0

    area = float((rightX - leftX) * (bottomY - topY))
    barea = (x12 - x11) * (y12 - y11) + (x22 - x21) * (y22 - y21) - area
    if barea <= 0: return 0
    return area/barea

def eval_bbox( bbox1, bbox2, thresh):
    """
    check if bbox1 & bbox2 is a pair of TP, according to label and conf
    bbox format: [x1,y1,x2,y2,conf,label]
    """
    if  bbox1[5] != bbox2[5]:
        return 0
    if cal_iou( bbox1[:4], bbox2[:4])  < thresh:
        return 0
    return 1

def eval_bbox_blind(bbox1, bbox2, thresh):
    """
    check if bbox1 & bbox2 is a pair of TP, according to label only
    bbox format: [x1,y1,x2,y2,conf,label]
    """
    if cal_iou( bbox1[:4], bbox2[:4])  < thresh:
        return 0
    return 1


def eval_multi_bbox( bboxes, gt_bboxes, thresh = 0.7, blind=False):
    """
    eval multiple bboxes 
    bboxes & gt_bboxes format: [bbox1,bbox2,bbox3...]
    return values:
        right: 
    """
    eval_fun = eval_bbox
    if blind:
        eval_fun = eval_bbox_blind

    num_gt = len(gt_bboxes)
    num_res = len(bboxes)

    found = [0]*num_gt
    right = [0]*num_res

    for i,bbox in enumerate(bboxes):
        for k, gt_bbox in enumerate(gt_bboxes):
            ret = eval_fun(bbox,gt_bbox, thresh)
            #print('******** bbox, gt_bbox *************')
            #print bbox, gt_bbox
            #print('*********************')
            if ret == 1:
                found[k] = 1.0
                right[i] = 1.0

    precision = float(sum(right)) / num_res
    recall = float(sum(found)) / num_gt


    return ( right, found, precision, recall)


