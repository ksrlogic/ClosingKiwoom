#영웅문 화면 기준입니다. 쓰고싶으시다면 LocationHelper를 이용하여 자신의 영웅문 화면마다의 
#각 창들의 좌표를 맞게 변경하여 사용하시면 됩니다.
#BMP 파일로 먼저 키움 화면을 저장하셔야합니다. BMP 파일 내에는 오늘 날짜의 문자열이 포함되어있어야 합니다.
#나머지는 전부 자동입니다.


import os
from datetime import date

#오늘 날짜, YYYYMMDD 형식
today = str(date.today()).replace("-","")
#현재 디렉토리 경로
directory = "../CapturedHero" 

#BMP파일 찾는 함수

def search_bmp_files(directory):
    bmplist = []
    
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".bmp"):
                file_path = os.path.join(root, file_name)
                print("찾은 BMP 파일:", file_path)
                
                bmplist.append(file_path)

    return bmplist


BmpList = search_bmp_files(directory)

#오늘 날짜의 BMP 파일 찾기
def isItToday(filelist,date):
    
    for file in filelist:
        if str(date) in str(file):
            
            return str(file)
# 함수 실행

image_root = isItToday(BmpList,today)
#지수 좌표
index_height = (960, 2200)
index_width = (6459, 7668)

index_location = [index_height, index_width]

#거래대금상위 좌표
ranking_height = (52, 675)
ranking_width = (3848, 4804)

ranking_location = [ranking_height, ranking_width]



#장중 코스피 지수 움직임 좌표
# Clicked at (x, y): 4539 1172
# Clicked at (x, y): 5340 2122

KospiMoveAndSAD_height = (1170,2200)
KospiMoveAndSAD_width = (4539, 5340)
KospiMoveAndSAD_location = [KospiMoveAndSAD_height, KospiMoveAndSAD_width]

#장중 코스닥 지수 움직임 좌표
# Clicked at (x, y): 5355 1171
# Clicked at (x, y): 6167 2124
KosdaqMoveAndSAD_height = (1170,2200)
KosdaqMoveAndSAD_width = (5355, 6167)
KosdaqMoveAndSAD_location = [KosdaqMoveAndSAD_height, KosdaqMoveAndSAD_width]


#외국인매매 좌표
# Clicked at (x, y): 4927 684
# Clicked at (x, y): 5665 1102

Foreigner_height = (684,1100)
Foreigner_width = (4927, 5665)
Foreigner_location = [Foreigner_height, Foreigner_width]

#기관 매매 좌표
# Clicked at (x, y): 5673 684
# Clicked at (x, y): 6413 1103
Firm_height = (684,1100)
Firm_width = (5673, 6413)
Firm_location = [Firm_height, Firm_width]

#관심종목 좌표
# Clicked at (x, y): 9 168
# Clicked at (x, y): 744 1181

Interest_height = (168,1200)
Interest_width = (0, 744)
Interest_location = [Interest_height, Interest_width]

#프로그램 신용융자 A

# Clicked at (x, y): 6981 557
# Clicked at (x, y): 7671 945

Program_height = (557,945)
Program_width = (6981, 7671)
Program_location = [Program_height, Program_width]