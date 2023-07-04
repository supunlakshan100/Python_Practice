i=3
while i<=100:
    
    i+=1
    if i % 2 == 0:
        continue
    print(i)
     


x=[-20,1,2,3,4,5,6,7,8,9,10,20]
max=x[0]
min=x[0]

for i in x:
    if max < i:
        max=i
    if min >i:
        min=i
        
print('max =',max)
print('min =', min)
    
  #iteration  
d= {
    'supun': 25,
    'kamal': 30,
    'nimal': 40,
    'sunil': 50,
    'saman': 60,
}
for name in d.items():
    print(name)
    
    
d={'colombo','galle','matara','kandy','jaffna'}
print(type(d))

#python function or methord

def get_grade(marks, subject='unknown'):
    print('subject=',subject)
    if marks >= 80:
        print('A')
    elif marks >= 60:
        print('B')
    elif marks >= 40:
        print('C')
    else:
        print('F')
        
get_grade(75, 'maths')

#packed arguments
def get_grade(*marks):
    
    total=0
    for i in marks:
        total +=i
        
    print(total)
    
get_grade(10,20,30,40,50,60,70,80,90,100,100)
    
    


