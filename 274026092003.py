
st = "PythonCode"
li = list(st)
li.sort()
a = ""
for i in sorted(set(li)):
    a = a + i + str(li.count(i))
print(a)
