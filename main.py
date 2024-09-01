import prettytable
from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Имя", "Фамилия", "Static ID", "Ранг", "Выслуга"]

print("BonusesProga [Version 1.2]")
print("(С) Timurkaaa Development")
print("\n")
print("Формат ввода данных:")
print("Имя Фамилия StaticID Ранг Выслуга:")
print("Введите данные(10 строк):")

str1 = input()
str2 = input()
str3 = input()
str4 = input()
str5 = input()
str6 = input()
str7 = input()
str8 = input()
str9 = input()
str10 = input()
table.add_row([str1.split()[0],str1.split()[1],str1.split()[2],str1.split()[3],str1.split()[4]])
table.add_row([str2.split()[0],str2.split()[1],str2.split()[2],str2.split()[3],str2.split()[4]])
table.add_row([str3.split()[0],str3.split()[1],str3.split()[2],str3.split()[3],str3.split()[4]])
table.add_row([str4.split()[0],str4.split()[1],str4.split()[2],str4.split()[3],str4.split()[4]])
table.add_row([str5.split()[0],str5.split()[1],str5.split()[2],str5.split()[3],str5.split()[4]])
table.add_row([str6.split()[0],str6.split()[1],str6.split()[2],str6.split()[3],str6.split()[4]])
table.add_row([str7.split()[0],str7.split()[1],str7.split()[2],str7.split()[3],str7.split()[4]])
table.add_row([str8.split()[0],str8.split()[1],str8.split()[2],str8.split()[3],str8.split()[4]])
table.add_row([str9.split()[0],str9.split()[1],str9.split()[2],str9.split()[3],str9.split()[4]])
table.add_row([str10.split()[0],str10.split()[1],str10.split()[2],str10.split()[3],str10.split()[4]])
print(table)
str11 = input()