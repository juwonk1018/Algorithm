import time
start = time.time()

for i in range(1000000):
    f = [float("inf")]
    f[0] = min(f[0], 3 + 323)

end = time.time()
print(end - start)


start = time.time()
for i in range(1000000):
    f = [0]
    f[0] = min(f[0], float("inf") + 323)
    
end = time.time()
print(end - start)