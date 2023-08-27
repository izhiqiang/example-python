import os

# 单个目录
def levelRename(fullpath, delstr):
    filelist = os.listdir(fullpath)
    i = 0
    for files in filelist:
        Olddir = os.path.join(fullpath, files)
        spfile = os.path.splitext(files)
        filename = spfile[0]  # 文件名
        fieltype = spfile[1]  # 文件后缀
        # 文件名截取
        newfilename = filename.split(delstr)[0]
        # 新的文件路径
        Newdir = os.path.join(fullpath, newfilename + fieltype)
        # 重命名
        os.rename(Olddir, Newdir)
        i += 1
    return i

# 多级目录
def levelsRename(fullpath, delstr):
    i = 0
    for fpathe, dirs, fs in os.walk(fullpath):
        for file in fs:
            Olddir = os.path.join(fpathe, file)
            spfile = os.path.splitext(file)
            print(Olddir)
            filename = spfile[0]  # 文件名
            fieltype = spfile[1]  # 文件后缀
            newfilename = filename.split(delstr)[0]
            Newdir = os.path.join(fullpath, newfilename + fieltype)
            os.rename(Olddir, Newdir)
            i += 1
    return i


if __name__ == '__main__':
    path = (r'需要更改的目录')
    delstr = "文件名字需要删除的字符串"
    filecount = levelsRename(path, delstr)
    print(filecount)
