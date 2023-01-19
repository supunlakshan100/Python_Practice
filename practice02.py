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
marks= 25
def get_grade(subject,marks):
    if marks >= 80:
        print('A')
    elif marks >= 60:
        print('B')
    elif marks >= 40:
        print('C')
    else:
        print('F')
get_grade('sinhala', 75)


