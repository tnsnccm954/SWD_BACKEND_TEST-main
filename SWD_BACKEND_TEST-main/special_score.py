"""
เขียนโปรแกรมอะไรก็ได้ที่อยาก present Python's skill set เจ๋ง ๆ ของตัวเอง
ข้อนี้ไม่ต้องทำก็ได้ ไม่มีผลลบกับการให้คะแนน แต่ถ้าทำมาเเล้วเจ๋งจริง ก็จะพิจารณาเป็นพิเศษ
"""
from random import randint
from terminaltables import AsciiTable

def randomReward(num):
    rewardednumber=''
    for i in range(num):
        j=randint(0,9)
        rewardednumber+=str(j)
    return rewardednumber    
        
lottery = input('Choose your Number[6]:')

while len(lottery)!=6:
    lottery = input('Again!,Choose your Number[6]:')

slot=[6,3,3,3,3,2]
rewarded=[]
for i in slot:
    rewarded.append(randomReward(i))

table_data = [
['Categories', 'Number','Rewards(BTH)'],
['First-Reward', rewarded[0],'6,000,000'],
['First-3-Num', rewarded[1]+' '+rewarded[2],'4,000'],
['Last-3-Num', rewarded[3]+' '+rewarded[4],'4,000'],
['Last-2-Num', rewarded[5],'2,000'],
]
table = AsciiTable(table_data)
print(table.table)


congrat="Congratulations, "
if lottery==rewarded[0]:
    congrat+='That\'s Your time for Retire. 6M .BTH'
elif rewarded[1] == lottery[0:3] or rewarded[2] == lottery[0:3]:
    congrat+='You see little sweettime. 4K .BTH'
elif rewarded[1] == lottery[3:6] or rewarded[2] == lottery[3:6]:
    congrat+='You see little sweettime. 4K .BTH'
elif rewarded[5]== lottery[4:6]:
    congrat+='You have to sleeps. 2K .BTH'
else:
    congrat+="May be next time be your."
print(congrat)