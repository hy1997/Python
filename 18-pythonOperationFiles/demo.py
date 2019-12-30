"""
file object = open(file_name [, access_mode][, buffering])
file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，
表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。

"R"  以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
"W"  原有内容会被删除。如果该文件不存在，创建新文件。 (覆盖)
"A" 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入（追加）
"""
# 指针
file = open("README")
file_write = open("README[附件]", "w")
# file.write("hello pyton", "GBK")

# text = file.read()

# 读取一行文件
while True:
    text = file.readline()
#     没有内容时退出循环
    if not text:
        break
    file_write.write(text)
    print(text)
print(text)
print(len(text))
print("-" * 50)

file.close()
file_write.close()
