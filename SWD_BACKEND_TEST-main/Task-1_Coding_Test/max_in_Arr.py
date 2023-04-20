"""
เขียนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน Array ด้วยภาษา python เช่น [1,2,1,3,5,6,4] 
ลำดับที่มีค่ามากที่สุด คือ index = 5 โดยไม่ให้ใช้ฟังก์ชั่นที่มีอยู่แล้ว ให้ใช้แค่ลูปกับการเช็คเงื่อนไข
"""
Arr=[1,2,1,3,5,6,4]
maximum=0
index_count=0
for i in Arr:
    if i > maximum:
        maximum=i
        index_count+=1
print('Maximum index on:',index_count)