import csv
import phonenumbers

with open("clients_list.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")

    with open("parsed_list.csv", "w") as parsed_csv:
        
        not_changed_fields = ["Имя", "Фамилия", "Отчество", "Должность", "Компания", "Ответственный"]
        fieldnames = not_changed_fields + ["Телефон"]

        csv_writer = csv.DictWriter(parsed_csv, delimiter=";", fieldnames=fieldnames)

        csv_writer.writeheader()
        for line in csv_reader:

            numbers = []

            numbers_in_line = line["Рабочий телефон"] + ", " + line["Мобильный телефон"]

            for match in phonenumbers.PhoneNumberMatcher(numbers_in_line, "RU"):

                phone_num = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)[1:]

                if phone_num in numbers:
                    continue
                numbers.append(phone_num)

                parsed_line = {name: value for name, value in line.items() if name in not_changed_fields}
                parsed_line["Телефон"] = phone_num

                csv_writer.writerow(parsed_line)

                