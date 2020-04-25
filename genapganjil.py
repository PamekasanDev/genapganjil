#!BrokenCode
import os
os.system("clear")
print "Program sederhana, menentukan bilangan genap-ganjil"
bilangan = input("Masukkan Bilangan: ")
if int(bilangan) % 2 == 0:
	print "%i adalah bilangan genap"%bilangan
else:
	print "%i adalah bilangan ganjil"%bilangan
