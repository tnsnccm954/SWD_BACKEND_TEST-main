
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).


notes
0,1,5,10,50,100,500,1000
1->IVX
2->XLC
3->CDM
"""


def roman_numeric(number):
    roman_unit=['','I','V','X','L','C','D','M']
    full_res =""
    length=len(number)
    if length==4 and int(number)==1000:
        print('M')
    elif length>=4 and int(number)>1000:
        print('Over 1000')
    else:
        unit=length*2
        for j in number:
            result=""
            for i in range(1,int(j)+1):
                if i==4:
                    result=roman_unit[unit-1]+roman_unit[unit]
                elif i==5:
                    result=roman_unit[unit]
                elif i==9:
                    result=roman_unit[unit-1]+roman_unit[unit+1]
                else:
                    result+=roman_unit[unit-1]
            full_res+=result
            unit-=2
        print(full_res)

num_Ro=input('Trans Num to Roman(1-1K,0->end):')
while int(num_Ro)!=0:
    roman_numeric(num_Ro)
    num_Ro=input('Trans Num to Roman(1-1K,0->end):')







