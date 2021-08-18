import settings_file_service


def obtain_user_data(question):
    return input(question)


def trigger_menu_flow():
    if settings_file_service.get_settings_file_location() == "No file defined":
        compose_user_menu()
    else:
        settings_file_service.load_settings_file()


def compose_user_menu():
    accountant_name = obtain_user_data("Podaj imię księgowej/księgowego:\n")
    accountant_surname = obtain_user_data("Podaj nazwisko księgowej/księgowego:\n")
    accountant_mail = obtain_user_data("Podaj adres email księgowej/księgowego:\n")
    search_mail_account = obtain_user_data("Podaj adres swój adres email, w którym szukać faktur:\n")
    search_invoice_directory = obtain_user_data("Podaj adres katalogu, w którym szukać faktur:\n")
    save_data = obtain_user_data("Czy chcesz zapisać dane do wykorzystania w kolejnych miesiącach (Y/N)?:\n")

    user_data = (
        ('accountant_name', accountant_name),
        ('accountant_surname', accountant_surname),
        ('accountant_mail', accountant_mail),
        ('search_mail_account', search_mail_account),
        ('search_invoice_directory', search_invoice_directory)
    )

    user_data_dict = dict(user_data)

    if save_data.lower() == 'y':
        save_path = input("Podaj ścieżkę (absolute path) zapisu pliku:\n")
        settings_file_service.add_invoice_setting_file_as_env_var(save_path)
        save_data_to_file(user_data_dict, save_path)
        print(f'File with settings has been save to : {save_path}')
    return user_data_dict


def save_data_to_file(user_data_to_file, file_path_to_save_data):
    with open(file_path_to_save_data, 'w') as save_data_file:
        for key, value in user_data_to_file.items():
            save_data_file.write(key + ':' + value + "\n")
