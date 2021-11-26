# from cron import sched
import sys,os,json
print(sys.platform)
s_str = sys.platform
with open('pid.json', 'r+', encoding='utf-8') as fp:
    j_pid = json.loads(fp.read())
if 'win' in s_str:

    for i in j_pid['pid']:

        result = os.popen(f'taskkill -PID {i} -F').read()
        print(result)
    with open('pid.json','w+',encoding='utf-8') as fp:
        fp.write(json.dumps({"pid": []}))
else:
    for i in j_pid['pid']:
        result = os.popen(f'kill -9 {i}').read()
        print(result)
    with open('pid.json', 'w+', encoding='utf-8') as fp:
        fp.write(json.dumps({"pid": []}))