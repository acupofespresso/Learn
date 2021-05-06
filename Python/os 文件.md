# Demo
```
import multiprocessing
import os
def copyFile(fileName,copyPath,pastePath):
    # 拼接拷贝路径
    copyPath = copyPath + fileName
    pastePath = pastePath + fileName
    # 以读取方式打开文件
    with open(copyPath,'rb') as copyPath:
        # 以写入方式打开文件
        with open(pastePath,'wb') as pastePath:
            while True:
                data = copyPath.read(1024)
                if data:
                    pastePath.write(data)
                else:
                    print('复制完成')
                    return
if __name__ == '__main__':
    copyPath = 'E://tos/'
    pastePath = 'E://pastetos/'
    try:
        # 创建目标文件，如已存在文件，则抛出异常
        os.mkdir('E://tos')
        print('创建目标文件')
    except:
        print('目标文件已存在')
    try:
        os.mkdir(pastePath)
        print('创建拷贝目录')
    except:
        print('拷贝目录已存在')
    # 获取文件列表
    fileList = os.listdir('E://tos/')
    print(fileList)
    # 遍历文件名
    for fileName in fileList:
        # 多进程拷贝文件
        fileProcess = multiprocessing.Process(target=copyFile,args=(fileName,copyPath,pastePath))
        fileProcess.start()
```