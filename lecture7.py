# # FILE I/O IN PYTHON
# # python can be used to perform operations on a file 

# # TYPES OF FILE
# #(1) TEXT FILE - .txt, .docx, .log
# #(2) BINARY FILE - .mp4, .mov, .png, .jpeg
# f = open("lect5.py", "r")
# data = f. read()
# print(data)
# print(type(data))
# f.close()

# #readline
f = open("demo.txt", "r")
line1 = f. readline()
print(line1)

f.close()