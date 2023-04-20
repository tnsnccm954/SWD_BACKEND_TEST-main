

"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python
โดยห้ามใช้ math.factorial เช่น 7! = 5040 มีเลข 0 ต่อท้าย 1 ตัว, 10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว
"""
number = int(input('Factorial:'))
sum_fac=1
zero_count=0
for i in range(1,number+1):
    sum_fac*=i
print('sum:',sum_fac)
while sum_fac%10==0:
    sum_fac/=10
    zero_count+=1
print('Zero Counter:',zero_count)
