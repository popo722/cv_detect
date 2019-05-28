# -*- coding: utf-8 -*-
import cv2
import sys

cap = cv2.VideoCapture(0)

# 分類器の特徴量を取得する
faceCascade = cv2.CascadeClassifier('./haarcascade_fullbody.xml')

while True:
    ret, frame = cap.read()

    width = 512
    height = 512
    # スクリーンショットを撮りたい関係で適当なサイズに縮小
    #image = cv2.resize(frame, (int(frame.shape[1]/3), int(frame.shape[0]/3)))
    image = cv2.resize(frame, (width, height))

    # 物体認識（人）の実行
    facerect = faceCascade.detectMultiScale(image, scaleFactor=1.01, minNeighbors=1, minSize=(30, 30))

    #検出した人を囲む矩形の作成
    for x, y, w, h in facerect:
        cv2.rectangle(image, (x, y),(x+w, y+h),(0,255,0), 2)

    # 加工済の画像を表示する
    cv2.imshow('Edited Frame', image)

    # キー入力を1ms待って、k が27（ESC）だったらBreakする
    k = cv2.waitKey(1)
    #k = cv2.waitKey(500)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
