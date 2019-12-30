import os
"""
os.name：返回当前使用平台的代表字符，Windows用 nt 表示，Linux用 posix 表示
os.listdir(path)：列举目录下的所有文件。返回的是list类型。
os.getcwd()：查看当前所在路径。
os.system(command)：函数用来运行shell命令。
os.curdir：返回当前目录（'.')
os.chdir(dirname)：改变工作目录到dirname
os.path.isfile(path)：检验给出的路径是不是文件。
os.path.isdir(path)：检验给出的路径是不是目录。
os.path.exists()：用来检验给出的路径是否真地存在
os.path.dirname(path)：返回文件路径
os.path.basename(path)：返回文件名
os.path.join(path, name)：连接目录与文件名或目录，使用‘\’连接
os.path.splitext()：分离文件名与扩展名
os.path.split(path)：将path分割成目录和文件名二元组返回。
os.path.normpath(path)：规范path字符串形式
os.path.abspath(name)：获得绝对路
os.path.getsize(name)：获得文件大小，如果name是目录返回0L
os.mkdir(path)：创建path目录（只能创建一级目录）
os.makedirs(path)：创建多级目录
os.remove(path)：函数用来删除一个文件。
os.rmdir(path)：删除path目录(只能删除一级目录，如'/Users/XXX/SSS'，只删除SSS目录)
os.removedirs(path)：删除多级目录(如'/Users/XXX/SSS'，必须为空目录，删除SSS、XXX目录)
os.path.getmtime(path)：返回文件或目录的最后修改时间，结果为秒数
os.path.getatime(path)：返回文件或目录的最后访问时间，结果为秒数
os.path.getctime(path)：返回文件或目录得创建时间，结果为秒数
os.sep：返回当前操作系统特定的路径分隔符
os.linesep：返回当前平台使用的行终止符
os.extsep：返回文件名与扩展名的分隔符
os.walk(top, topdown=True, onerror=None, followlinks=False)
"""

print(os.listdir("../"))
