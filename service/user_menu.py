def obtain_user_data(question):
    return input(question)


def compose_user_menu():
    accountant_name = obtain_user_data("Podaj imię księgowej/księgowego:\n")
    accountant_surname = obtain_user_data("Podaj nazwisko księgowej/księgowego:\n")
    accountant_mail = obtain_user_data("Podaj adres email księgowej/księgowego:\n")
    search_mail_account = obtain_user_data("Podaj adres swój adres email, w którym szukać faktur:\n")
    search_invoice_directory = obtain_user_data("Podaj adres katalogu, w którym szukać faktur:\n")
    save_data = obtain_user_data("Czy chcesz zapisać dane do wykorzystania w kolejnych miesiącach (Y/N)?:\n")

    user_data = (accountant_name, accountant_surname, accountant_mail, search_mail_account, search_invoice_directory)

    if save_data.lower() == 'y':
        save_data_to_file(user_data, input("Podaj ścieżkę zapisu pliku:\n"))
    else:
        return user_data


def save_data_to_file(user_data_to_file, file_path_to_save_data):
    with open(file_path_to_save_data, 'w') as save_data_file:
        for answer in user_data_to_file:
            save_data_file.write(answer + "\n")
