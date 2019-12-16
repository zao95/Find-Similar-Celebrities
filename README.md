# Find-Similar-Celebrities
자신이 어떤 연예인과 닮았는지 알아볼 수 있는 프로그램입니다.
DB에 한국의 유명 연예인들을 주로 담았기 때문에, 비한국인의 경우 정확도가 떨어질 수 있습니다.

This repository is a program to find out what kind of celebrity you look like.
Since Korea's famous celebrities are included in the database, accuracy can be reduced for non-Koreans.

## Usage
정말 죄송하게도, 저의 실력부족으로 인해 패키징을 하지 못했습니다.
실행은 파이썬을 통해 해야하며, 설치해야하는 라이브러리는 [Dependencies](#dependencies)에 작성해두었습니다.
실행 전 설정해야하는 부분은 [Setting](#setting)에 작성해두었습니다.

I'm really sorry, but I couldn't package it because of my lack of skills.
You must run it through Python, and you have created a library in Dependencies that you need to install.
The parts that need to be set before execution have been created in Setting.

## Dependencies
python==3.6.3
opencv-contrib-python==3.4.2.16
opencv-python==3.4.2.16
glob3==0.0.1
matplotlib==3.1.2
icrawler==0.6.2

## Setting
실행 전 설정해주어야하는 부분은 메인의 10:11입니다.
```python
# Setting
db_create = True
ratio = 0.75
```
db_create 변수는 boolean으로, 첫 실행이나 연예인 이름 리스트가 변경되었을때만 True로 변경해주면 됩니다.
ratio는 정밀도로, 0에 가까워질수록 정밀해지지만, 아예 에러가 날 확률도 커집니다.

10:11 of the main part of who should be set before running.

The db_create variable is boolean, which is only changed to True if the first run or the list of celebrity names is changed.
The ratio is precision, and the closer it gets to zero, the greater the probability of an error.

## License
[WTFPL](http://www.wtfpl.net)