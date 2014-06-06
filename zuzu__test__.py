mydict = {'sape': 4139, 'jack': 4098, 'guido': 4127}
def sortByKey(dict):
    returnlist = sorted(dict.items(), key = lambda t:t[0])
    print returnlist 

def sortByValueDesc(dict):
    returnlist = sorted(dict.items(), key = lambda t:t[1], reverse=True)
    print returnlist
    
sortByKey(mydict)
sortByValueDesc(mydict)


def fibonacci(n):
	a, b, count = 0, 1, 0
	while count < n:
		a, b = b, a+b
		yield a
		count = count +1
f = fibonacci(10)
for x in f:
    print x
print

def fibonacciVersion2():
    a, b = 0, 1
    while True:
        a, b = b, a+b
        yield a
f = fibonacciVersion2();
count = 0
for x in f:
    print x
    count +=1
    if(count >= 10): break
print

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [element for element in numbers if element > 0]
print newlist