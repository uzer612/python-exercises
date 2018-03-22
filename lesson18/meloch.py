def takeLargeBanknotes(banknotes):
	a = []
	for i in banknotes:
		if i > 10:
			a.append(i)
	return a

