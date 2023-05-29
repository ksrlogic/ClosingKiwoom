import requests
from bs4 import BeautifulSoup
import pyautogui

# 웹 페이지에 접속하여 HTML 가져오기
url = 'https://kr.investing.com/indices/nq-100'  # 대상 웹사이트 URL 입력
response = requests.get(url)
html = response.text

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html, 'html.parser')

# 원하는 요소를 찾아서 캡처
target_element = soup.find('div', class_='schedule')  # 원하는 요소 선택 (예: <div class="schedule">...</div>)
element_location = target_element.location  # 요소의 위치 정보 가져오기
element_size = target_element.size  # 요소의 크기 정보 가져오기

# 캡처할 영역의 좌표 계산
x = element_location['x']
y = element_location['y']
width = element_size['width']
height = element_size['height']

# 캡처 실행
screenshot = pyautogui.screenshot(region=(x, y, width, height))

# 이미지 저장
screenshot.save('captured_schedule.png')