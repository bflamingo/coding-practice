def naive_search(T,P):
	matches = []
	for i in range(len(T)-len(P)+1):
		for j in range(len(P)):
			if T[i+j] != P[j]: #character doesn't match
				break
			else: # character matches
				if j == len(P)-1: # match found
					matches.append(i)
				else:
					continue
	return matches

def KMP_table(P):
	O = [0 for _ in P]
	for i in range(1,len(P)):
		done = False
		O[i] = O[i-1]
		while not done:
			if P[i] == P[O[i]]:
				O[i] = O[i] + 1
				done = True
			else:
				if O[i]-1 < 0:
					done = True
				else:
					O[i] = O[O[i]-1]

	return O

def KMP(T,P):
	O = KMP_table(P)
	matches = []
	i = 0
	tj = 0
	while i <= len(T) - len(P) + 1:
		for j in range(tj, len(P)):
			if P[j] == T[i+j]:
				if j == len(P)-1: # match found
					matches.append(i)
					i = i + j - O[j-1]
					tj = 0
				else:	#do nothing, continue to next iteration
					pass

			else:
				if j==0:
					i = i + j + 1
					tj = 0
				elif O[j-1]==0:
					i = i + j
					tj = 0
				else:
					i = i + j - O[j-1]
					tj = O[j-1]
				break

	return matches


T1 = "ABC ABCDAB ABCDABCDABDE"
P1 = "ABCDABD"

T2 = "banananabanaba nabanana"
P2 = "banana"

T3 = "abcabcabcabc"
P3 = "abcabc"

P = "abeabdabeabe"

print(KMP(T1,P1))
print(KMP(T2,P2))
print(KMP(T3,P3))