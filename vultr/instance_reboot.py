import requests
import datetime, time
from apscheduler.schedulers.background import BackgroundScheduler


#현재시각 함수
def now_time():
    return '({})'.format(datetime.datetime.now().strftime('%y/%m/%d %H:%M:%S'))

#constants
api_key = input("Enter your VULTR API KEY ==>")
t = input("What time do you want reboot?(every day) (hours:minute:second) (ex) 13:00:00 \n==>")
h = t.split(':')[0]
m = t.split(':')[1]
s = t.split(':')[2]

# request setting
url = "https://api.vultr.com/v2/instances"
url_reboot = "https://api.vultr.com/v2/instances/reboot"
headers = {"Authorization": "Bearer {}".format(api_key),
           "Content-Type": "application/json"}

# reboot function
def instance_reboot():
    response = requests.get(url, headers=headers)

    L=len(response.json()['instances'])

    instances = []

    for i in range(L):
        instances.append({'id':response.json()['instances'][i]['id'], 
                        'label':response.json()['instances'][i]['label'], 
                        'ip':response.json()['instances'][i]['main_ip']})

    instances_ids = []

    for i in range(L): 
        id = instances[i]["id"]
        if id[-6:] != 'reboot':
            instances_ids.append(instances[i]["id"])

    data = {"instance_ids" : instances_ids}

    requests.post(url_reboot, json=data, headers=headers)

    print("instances reboot complete!\n")


#알림시간설정
sched = BackgroundScheduler()

@sched.scheduled_job('cron', hour=f'{h}', minute=f'{m}', second=f'{s}', id='reboot')
def job1():
    instance_reboot()

sched.start()


#main
def main():
    print('매일 {}:{}:{}에 재부팅할 예정입니다. *현재시각 {}'.format(h,m,s,now_time()),end='\r')
    time.sleep(1)


if __name__=="__main__":
    print("\n\n*** welcome to the SITPO world! ***\n\n")
    while True:
        main()