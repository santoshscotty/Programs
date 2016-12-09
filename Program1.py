print 'Enter the max number of versions.'
NoOfVersions=int(raw_input())
a=list()
def ADD(b):
    global a
    n=len(a)
    if n<NoOfVersions:
        a.append(b)
    else:
        for val in a:
            if a.index(val)!=0:
                a[a.index(val)-1]=val
        a[-1]=b
    print 'Added'
def GET(b=0):
    global a
    if b<NoOfVersions:
        print 'Output:\nkey '+a[(b*(-1))-1]
    else:
        print 'Invalid Version Specified'
def DELETE():
    global a
    a=list()
    print 'All Versions are Deleted'
x=''
while x!='0':
    print '1. ADD(key,value)\n2. GET(key,version no)\n3. DELETE(key)\n4. Print all the values\nAny other values to Exit\nEnter your Choice'
    x=int(raw_input())
    if x==1:
        print 'Enter the value to add'
        y=raw_input()
        ADD(y)
    elif x==2:
        print 'Which number of previous version would you like to see?? Enter null if current version.'
        y=raw_input()
        if y=='':
            GET()
        else:
            GET(int(y))
    elif x==3:
        DELETE()
    elif x==4:
        print 'Output:'
        for y in a:
            print y
    else:
        print 'Invalid Choice, Exitting..'
        break;
