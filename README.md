# 겜린더 푸시 알림 자동화
달력에 등록한 게임에 대한 출시 알림을 주기 위한 자동화 스크립트

Github Action을 이용해서 구현

사용자가 달력에 등록해 둔 게임 목록는 Redis에 저장되는데, 
Redis에 있는 내용들을 정리해 가져와서 푸시 알림으로 전송해줍니다.

보안을 위해 외부에서는 Redis에 접근하지 못하게 만들어뒀기 때문에 VPN을 사용하여 접근하게 만들었습니다.


## Status
[![Gamlendar Game Notification Workflow](https://github.com/munhyok/gamlendar_fcm/actions/workflows/scheduled_workflow.yml/badge.svg)](https://github.com/munhyok/gamlendar_fcm/actions/workflows/scheduled_workflow.yml)

## 과정
### 1. 파이썬 설치

### 2. requirements.txt에 있는 의존성 설치

### 3. Wireguard 설치

### 4. Wireguard config 생성

### 5. Wireguard 연결

### 6. Firebase Service Account.json 추가

### 7. 파이썬 main.py 실행

### 8. Firebase Service Account.json 삭제



