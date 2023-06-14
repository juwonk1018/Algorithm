traps=[2,3,4]

mask_idx = {t : n for n, t in enumerate(traps)}
print(mask_idx)

print(1<<0)
print(1<<1)
print(~(1<<2))

dist = {(1,2) : 3}
print(dist[(1,3)])