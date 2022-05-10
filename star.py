#la valeur de n pour une etoile commplete est egal 7 (n=7)
n = int(input("entrer le nombre de ligne:"))
for row in range(n):
	for col in range(n+2):
		if row + col == n-3 or (row == n-5 and col < n-5 or row == n-5 and col > n-1) or (row == n-3 and col == n-6 or row == n-3 and col == n) or col - row  == n-3 or row - col== n-5 or row + col== n+3 :
			print("*",end="")
		else:
			print(end= " ")
	print()


