import sys

message = ' '.join(sys.argv[1:]) or "hello world!"

print(sys.argv[1:])
a = b'firstmessage'
a = a.decode('utf-8')
print(a.count('.'))

print('aaa' + 'bbb')
sStr1 = 'strcpy'
sStr2 = sStr1
sStr1 = 'strcpy2'
print(sStr2)

for a in range(1, 5):
    f = ':' + '' + '%s' % ('.' * a)
    print(f)

a=[1,2,3,4]
print(a[1:])