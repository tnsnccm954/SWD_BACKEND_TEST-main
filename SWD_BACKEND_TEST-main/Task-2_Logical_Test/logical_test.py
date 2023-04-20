
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
def numberTH(number,length,last):
    numTh=['ศูนย์','หนึ่ง','สอง','สาม','สี่','ห้า','หก','เจ็ด','แปด','ก้าว']
    if length==1 and number<=2:
        if number==2:
            result="ยี่"
        elif number==1:
            result=''
    elif length==0 and len(last)>2 and number==1:
            result="เอ็ด"
    else:
        result= numTh[number]
    return result

def num_Th(num):
    unit=['','สิบ','ร้อย','พัน','หมื่น','แสน','ล้าน']
    result=""
    length = len(num)-1
    for i in num:
        result+=numberTH(int(i),length,result)
        if length>=1:
            result+=unit[length]
        length-=1   
    print(result) 
    
numInput = input('แปลงอาราบิก->เลขไทย (0-10M,-1->end):') 
while int(numInput)!=-1:
    if len(numInput)>7:
        print("--เลขเกินกรุณากรอกใหม่--")
    else:
        num_Th(numInput)
    numInput = input('แปลงอาราบิก->เลขไทย (0-10M,-1->end):')  
    

