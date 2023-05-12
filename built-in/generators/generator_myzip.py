def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    return (tuple(S[i] for S in seqs) for i in range(minlen))

seqs = [[1, 2, 3], [4, 5, 6, 7], [9, 10, 11]]

gen = myzip([1, 2, 3], [4, 5, 6, 7], [9, 10, 11])
print(next(gen))
print(next(gen))
print(next(gen))
