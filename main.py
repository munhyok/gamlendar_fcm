import firebase_admin
from firebase_admin import credentials, messaging
from src.redis_conn import reDB
from datetime import datetime
import pytz
import json


def initializeToday():
    kst = pytz.timezone('Asia/Seoul')
    today_date = datetime.now(kst)
    formatted_date = today_date.strftime('%Y-%m-%d')
    return formatted_date

def initializeFirebase():
    #cred = credentials.Certificate("./credentials/serviceAccountKey.json")
    cred = credentials.Certificate("./serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    print('firebase initialized')


def key_prefix_dateList(date):
    key_prefix = reDB.keys(f"{date}:*") 
    
    return key_prefix

def id_game_prefix(user_gameList: list):
    #print(len(user_gameList))
    
    prefix_list = []
    
    for user_id in user_gameList:
        
        id = user_id.split(':')
        id = id[1]
        
        # user_id별 달력에 저장한 게임 목록 불러오기
        game_dict = reDB.hscan(user_id)[1]
        
        gameList = game_dict.values()
        gameList = list(gameList)
        
        
        id_list_prefix = {id:gameList}
        
        prefix_list.append(id_list_prefix)
        
        #print(id_list_prefix)
        
    return prefix_list
        

def message_template(gameList):
    length = len(gameList)
    
    if length == 1:
        return f"{gameList[0]}"
    
    return f"{gameList[0]} 외 {length-1}개의 게임"
    

def notification_message(user_id, gameList):
    #user_id = '6747640125dad51236dec3af' # Test용도, Live에선 주석 처리
    message = messaging.Message(
        topic=user_id,
        notification=messaging.Notification(
            title='게임 출시 알림',
            body=message_template(gameList)
        ),
        
        android=messaging.AndroidConfig(
                notification=messaging.AndroidNotification(
                    channel_id="500"
                )
            )
        
    )
    
    return message
    
def send_all_msg(messageList):
    
    try:
        response = messaging.send_each(messageList, dry_run=False)
        print(f"Successfully sent {response.success_count} messages")
        print(f"Failed to send {response.failure_count} messages")

        for i, resp in enumerate(response.responses):
            if resp.success:
                print(f"Message {i+1}: Success")
            else:
                print(f"Message {i+1}: Failed - {resp.exception}")
    except:
        print('알림 전송할 유저가 없습니다...')
        
        

        
def main():
    
    messageList = []
    
    today = initializeToday()
    print(f"오늘 날짜: {today}")
    initializeFirebase()
    
    redis_isconnect = reDB.ping()
    print(redis_isconnect)
    
    user_gameList = key_prefix_dateList(today)
    
    id_list_prefix = id_game_prefix(user_gameList)
    
    for msg in id_list_prefix:
        for key, value in msg.items():
            #print(f"{key}: {value}")    
            message = notification_message(key, value)
            #print(f"Generated Message: {message}")
            messageList.append(message)
    
    #print(messageList)
    send_all_msg(messageList)


if __name__ == '__main__':
    main()
        
