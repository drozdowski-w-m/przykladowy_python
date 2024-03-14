from datetime import datetime

print("***************************")
print("****      Witaj w      ****")
print("****    Sklepie ZOO    ****")
print("***************************")

inwentarz = {
	"pies": 10,
	"kot": 8,
	"ptak": 25,
	"iguana": 2
}

sumaZwierzat = 0
for val in inwentarz.values():
	sumaZwierzat += val
	

print("Podaj swoje imie")
imie = input()
print("Podaj swoje nazwisko")
nazwisko = input()

#Konkatanacja
daneKompletne = imie + " " + nazwisko
print("Dzieki za odwiedziny ", daneKompletne)

historiaZakupow = []

def pokazMenu():
	print("")
	print("Wybierz opcje: ")
	print("1: Stan zwierzat w sklepie.")
	print("2: Kup zwierze.")
	print("3: Wyswietl zakupy.")
	print("4: Zakoncz program.")
	
def pokazInwentarz():
	print("Stan:")
	for nazwa, ilosc in inwentarz.items():
		print(f"   >>> {nazwa}: {ilosc}")
	print("Lacznie ", sumaZwierzat," zwierzat")

def kupZwierze():
	koszyk = []
	while True:
		print ("Jakie zwierze chcesz kupic? (max 1 z kazdego gatunku)")
		print("Wpisz 'k' aby zakonczyc lub 'w' zeby wyswietlic zawartosc koszyka")
		
		jakiZwierz = input()
		
		if jakiZwierz == "k":break
		
		if jakiZwierz == "w":
			print(f"Twoj koszyk zawiera {koszyk}")
			continue

		if jakiZwierz not in inwentarz:
			print(f"W inwentarzu nie mamy {jakiZwierz}")
		elif inwentarz[jakiZwierz] == 0:
			print(f"Niestety {jakiZwierz} sie wyprzedal")
		elif jakiZwierz not in koszyk:
			koszyk.append(jakiZwierz)
		else:
			print("Takiego juz masz w koszyku")
		#print("Kupiles ... ", jakiZwierz)
	
	print("Zawartosc koszyka:")
	for zwierze in koszyk:
		print(">>> ",zwierze)
		inwentarz[zwierze] -= 1

	obecnaData = datetime.now()
	historiaZakupow.append( (imie, koszyk, obecnaData) )
		
def pokazZakupy():
	print("")
	print("**** TWOJE ZAKUPY ****")
	for zakup in historiaZakupow: #zakup to krotka
		print(f"    {zakup[0]} kupil {zakup[1]} w dniu {zakup[2]}")
	

while True:
	pokazMenu()
	odp = input()

	if odp == "1":
		pokazInwentarz()
	elif odp == "2":
		kupZwierze()
	elif odp == "3":
		pokazZakupy()
	elif odp == "4":
		print("Program zakonczony")
		break