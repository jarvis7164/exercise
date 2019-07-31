#比较两个文件，并把相同的内容输入到第三个文件中
#打开文件1，逐行读取
file1 = input('请输入第一个文件名：')
file2 = input('请输入第二个文件名：')
f1=open(file1,'r',encoding='utf-8')
lines_a=f1.readlines()

#打开文件2，逐行读取
f2=open(file2,'r',encoding='utf-8')
lines_b=f2.readlines()

#写入相同内容到文件new.txt
file3 = 'new.txt'
out_file = open(file3,'w')

#用for遍历，并分割
for line_a in lines_a:
    column_a= line_a.strip().split(',')#获取第一行的数据列表，按照逗号分隔
    # print(column_a)
    for line_b in lines_b:
        column_b=line_b.strip().split(' ')
#根据第二列内容判断
        if column_a[0]==column_b[0]:
            out_file.write(line_b)
#关闭文件
f1.close()
f2.close()
