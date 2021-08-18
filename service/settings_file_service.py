import os


def add_invoice_setting_file_as_env_var(save_path):
    os.environ["INV_AUTOMATION_TOOL_SETTING_FILE"] = save_path


def get_settings_file_location():
    return os.environ.get("INV_AUTOMATION_TOOL_SETTING_FILE", "No file defined")


def read_settings_file(save_path):
    with open(save_path, 'r') as settings_file:
        lines = settings_file.readlines()
        [print(line) for line in lines]


def load_settings_file():
    if get_settings_file_location() != "No file defined":
        load_settings_answer = input("Znaleziono plik z zapisanymi danymi. Czy zastosować? (Y/N): \n")
        if load_settings_answer.lower() == 'y':
            read_settings_file(get_settings_file_location())
