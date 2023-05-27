# ClosingKiwoom
파이썬으로 만든 마감 시황 정리 캡쳐 자동화 도구


준비:

![image](https://github.com/ksrlogic/ClosingKiwoom/assets/63966461/a838ed47-6fe2-4b05-9109-5a7821fc05ce)


영웅문4의 화면 캡쳐 기능을 다음과 같이 설정해주시기 바랍니다.

대상 경로는 다운받은 파일의 CapturedHero 폴더입니다.


그다음 Roots 파일로 이동합니다.

![image](https://github.com/ksrlogic/ClosingKiwoom/assets/63966461/f650b984-e0fb-4675-820a-5faef5b1c147)

내리다보면 이런 코드를 볼 수 있을 것입니다.

숫자들이 좌표값이고, 이 좌표값들을 자신의 모니터 화면에 맞게 조정하면 됩니다.



LocationHelper.py 로 들어갑니다.
![image](https://github.com/ksrlogic/ClosingKiwoom/assets/63966461/71203985-6d44-4443-a34a-58b6d77af548)

LocationHelper.py는 캡쳐할 화면의 좌표를 알려주는 도구입니다.
실행 후 이미지가 나오면, 마우스 커서로 이미지의 원하는 곳의 좌표값이 터미널에 print됩니다.


![image](https://github.com/ksrlogic/ClosingKiwoom/assets/63966461/6c47b777-c8d3-43e3-a0a0-9ecbc1e9defc)

이것을 구하여 Roots파일에 있는 좌표값들을 변경해주시면 됩니다.

![image](https://github.com/ksrlogic/ClosingKiwoom/assets/63966461/b49479ff-81e4-48fe-8a2a-d111e9fb2719)


예로 내 영웅문4 화면의 시간대별업종지수 화면을 LocationHelper를 통해 좌표를 구했다면, (적은 수치, 큰 수치) 로 입력해주시면 됩니다.
순서대로 세로와 가로입니다.


![image](https://github.com/ksrlogic/ClosingKiwoom/assets/63966461/5661b3e5-a08a-4719-9fa5-856312c0dbc2)


Main.py의 이 부분을 수정하면 더 많은 화면들을 저장할 수 있습니다.

사용해보면 코드가 쉽기 때문에 이해가 갈 것입니다. 자유롭게 수정하여 사용하시면 됩니다.


