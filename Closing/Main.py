import cv2
import Roots
import os

from datetime import date
from Roots import *

today = str(date.today()).replace("-","")

#금일 날짜 폴더 생성
if os.path.exists("../CapturedHero/{}".format(today)):
    pass
else:
    print("폴더가 존재하지 않습니다.")
    os.mkdir("../CapturedHero/{}".format(today))
    
#영웅문 캡쳐 이미지 변수 정의
Heroimage = cv2.imread(Roots.image_root)

#캡쳐 좌표 모음 인덱스
locations = [index_location,
             ranking_location,
             KospiMoveAndSAD_location,
             KosdaqMoveAndSAD_location,
             Foreigner_location,
             Firm_location,
             Program_location]

names = ["Index",
         "Ranking",
         "Kospi",
         "Kosdaq",
         "Foreigner",
         "Firm",
         "Program"]

#이미지 크롭 함수
def cropper(imageOrigin, location):
    
    print(location)
    cropped_image = imageOrigin[location[0][0]: location[0][1],
                          location[1][0]: location[1][1]]
    
    
    return cropped_image

#이미지 저장 함수
def saver(image, date, name):
    #이미지 생성 날짜 및 이름 저장
    cv2.imwrite('../CapturedHero/20230527/{}_{}.png'.format(date,name), image)
    

#메인

for index, location in enumerate(locations):
    #이름 정의
    name = names[index]
    
    cropped_image = cropper(Heroimage, location)
    cv2.imshow('Cropped Image', cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    saver(cropped_image, today, name)