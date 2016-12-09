def CheckInFile(filename,Url):
    f=open(filename,'r')
    OldUrl=f.readline()
    count=0
    while OldUrl!="":
        if OldUrl.split('\t')[0].strip()==Url.strip():
            count+=1
        OldUrl=f.readline()
    f.close()
    return count
file2=open('File2','r')
url=file2.readline()
file3=open('custom','w')
file3.close()
while url!="":
    n=CheckInFile('File2',url)
    if CheckInFile('custom',url)==0:
        file3=open('custom','a')
        file3.write(url.strip()+"\t"+str(n)+'\n')
        file3.close()
    url=file2.readline()
print'Stats for today\n\nUrlh\t#of Repetitions'
file3=open('custom','r')
line=file3.readline()
while line!="":
    print line.strip()
    line=file3.readline()
file3.close()
print '\nUrlhs which are Repeatedly crawled'
file3=open('custom','r')
line=file3.readline()
while line!="":
    line=line.split('\t')[0]
    if CheckInFile('File1',line)!=0:
        print line
    line=file3.readline()
file3.close()
