list = []
for i in range(901, 1000):
    for j in range(901,1000):
        x = i * j
        l = x
        r = 0
	rev = 0

        while l > 0 :
                r = l % 10
                rev = l // 10
                rev = rev * 10 + r
                if rev == x :
                         list.append(rev)
print(max(list))               

