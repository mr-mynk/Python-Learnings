from collections import namedtuple,deque,defaultdict,Counter,OrderedDict
'''
# Unpacking sequence
records = [('foo',1,2),('bar','hello'),('foo',3,3)]

def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)

for tag,*args in records:
    print('-------------------loop',records.index((tag,*args))+1)   
    print('tag :',tag)
    print('args :',args)
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
print('--------================-------')
s = 'ljutlgvrffudnecktcjrdfikhdntdvrd'

f,*m,l = s
print(f,*m,l)
print(m)



# collections class 
# namedtuble, deque(double-ended queue), Counter, defaultdict, OrderedDict


print('-------------------=============== namedtuple ==============---------------')

Point3D = namedtuple('Point', ['x', 'y', 'z'])
p = Point3D(10, 20, 30)

print(p.x)      # Output: 10
print(p.y)      # Output: 20
print(p[2])     # Output: 30

# You can also use namedtuple to create a list of points
points = [Point3D(1, 2, 3), Point3D(4, 5, 6)]
for point in points:
    print(f"x: {point.x}, y: {point.y}, z: {point.z}")

print(type(p),type(points),type(Point3D),sep='\n')


Flat = namedtuple('Flat',['B','H','K'])
f1 = Flat(2,1,1)
print('f1-',f1)
print('flat-',Flat)
Flats = []
for i in range(3):
    x,y,z = input("x : "),input("y : "),input("z : ")
    Flats.append(Flat(x,y,z))

for i in Flats:
    print(f'Flats{Flats.index(i)+1} having : {i.B}B {i.H}H {i.K}K')

print('---------=========== deque =======-------')
lst = [i for i in range(1,11)]
print('lst : ',lst,type(lst))
dq = deque(lst)
print('dq : ',dq,type(dq))

dq.appendleft(0)
print('append left on dq : ',dq,type(dq))
dq.popleft()
print('popleft on dq :',dq,type(dq))

print('----------------===================== Counter ================-----------------')
b, *args = 'aJsfjlksjfls'
print('args list : ',args,type(args))
print('count of each : ',Counter(args))
print('count of j : ',Counter(args).get('j'))

print('Items : ',end="\n"),[print(i) for i in Counter(args).items()]

print('most common : ',Counter('abacdasddasdsdasdadsdasdasdadasd').most_common(3))
print('counter dict: ',Counter('afdsfasfdfasdadsfadfasfsa'))
print('value : ',Counter('afdsfasfdfasdadsfadfasfsa').values())

c = Counter('apple')
print(f"Initial Counter: {c}")

new_counts = {'a': 3, 'p': 1, 'z': 5}
c.update(new_counts)
print(f"Updated Counter: {c}")
print("updated c: ",c)



print('----------------===================== defualtdict ================-----------------')
# lst = [('a',1),('b',2),('c',3)]

data = [('a', 1), ('b', 2), ('a', 3), ('c', 4)]
grouped_data = defaultdict(list)

for key, value in data:
    grouped_data[key].append(value)

grouped_data["b"]=0
print(grouped_data)
# Output: defaultdict(<class 'list'>, {'a': [1, 3], 'b': [2], 'c': [4]})



with open('Practical/files/file.txt','w+') as f:
    [f.write('klsafhwevnalcwuilrhlfncn. l fhcn whfcnfliwec\n') for i in range(5)]
print('--------------------------------------')
with open('Practical/files/file.txt','r+') as f1:
    print('f1: ',f1,type(f1))
    print('f1 lst: ',list(f1))
    for i in f1:
        print('i: ',i,type(i))

'''

