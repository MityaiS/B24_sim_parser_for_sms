import csv

with open("clients_list.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")

    with open("parsed_list.csv", "w") as parsed_csv:
        
        fieldnames = ["Имя", "Фамилия", "Отчество", "Должность", "Компания", "Ответственный", "Рабочий телефон", "Мобильный телефон"]

        csv_writer = csv.DictWriter(parsed_csv, delimiter=";", fieldnames=fieldnames)

        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow({name: value for name, value in line.items() if name in fieldnames})