import cv2
import Roots

#이미지의 좌표를 탐색할 때 도와주는 프로그램입니다.


# 마우스 클릭 이벤트 핸들러 함수
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 마우스 버튼 클릭 시
        print("Clicked at (x, y):", x, y)

# 이미지 로딩
image = cv2.imread(Roots.image_root)

# 이미지 표시 및 마우스 이벤트 콜백 함수 등록
cv2.imshow('Image', image)
cv2.setMouseCallback('Image', mouse_callback)

# 키 입력 대기
cv2.waitKey(0)
cv2.destroyAllWindows()