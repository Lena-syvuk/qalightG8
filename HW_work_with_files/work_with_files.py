import xmltodict
from dict2xml import dict2xml
import json

test_dict = {
    'user1': {'gender': 'm',
              'firstname': 'Vasya',
              'lastname': 'Pupkin',
              'age': 20},
    'user2': {'gender': 'f',
              'firstname': 'Vasilisa',
              'lastname': 'Pupkina',
              'age': 21}
}
# first_task - Збереження словника у форматі XML: Конвертуйте словник у формат XML та збережіть його у файл з розширенням ".xml"
xml_output = dict2xml(test_dict, wrap="root", indent="  ")
with open('file_xml.xml', 'w') as file:
    file.write(xml_output)

# Task_2 - Читання XML-файлу: Відкрийте XML-файл та розпарсіть його, щоб отримати знову словник Python як оригінал.
with open('file_xml.xml', 'r') as file:
    xml_content = file.read()
    my_dict = xmltodict.parse(xml_content)
    print(my_dict)

# task_3 - Збереження словника у форматі JSON: Конвертуйте словник у формат JSON та збережіть його у файл з розширенням ".json".
json_data = json.dumps(test_dict)

with open('json_data.json', 'w') as file:
    file.write(json_data)

# task_4 - Читання JSON-файлу: Відкрийте JSON-файл та завантажте його дані у Python як словник.
with open('json_data.json', 'r') as file:
    data = json.loads(file.read())
    print(data)


# Task_5 - Конвертація з XML до JSON: Завантажте XML-файл, розпарсіть його та конвертуйте у формат JSON. Потім збережіть в файл.
with open("file_xml.xml", "r") as file:
    data_dict = xmltodict.parse(file.read())
    json_data = json.dumps(data_dict)
with open("my.json", "w") as json_file:
    json_file.write(json_data)






