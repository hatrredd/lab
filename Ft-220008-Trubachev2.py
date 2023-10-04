name = input("Как вас зовут?\n")
year = int(input("Сколько вам лет?\n"))
if int(year) < 1:
    year = input("Введите корректный возраст\n")
country, city = map(str, input("Ваша страна и город проживания: ").split(","))
print("Уважаемый", name+"!\n\nНа сегодняшний день Вы проживаете в стране", country, "в городе", city+ ", и вы родились в", 2023-int(year), "году")