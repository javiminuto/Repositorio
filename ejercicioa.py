row = 8
cols = 4

m = []
for i in range(row):
    r = []
    for j in range(cols):
        r.append(i*cols+j)
    m.append(r)
print(m)