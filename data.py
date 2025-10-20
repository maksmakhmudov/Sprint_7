class Data:
    valid_login = 'Petrovcky12'
    valid_password = '987654321pass'
    valid_firstname = 'Serj'
    valid_courier_data = {'login': 'Petrovcky', 'password': '987654321pass', 'firstName': 'Serg'}
    courier_data_without_name = {'login': 'Petrovcky', 'password': '987654321pass'}
    courier_data_with_wrong_password = {'login': 'Petrovcky', 'password': '987654321pass'}


class OrderData:
    order_data_grey_1 = {
        'firstName': 'Софа',
        'lastName': 'Васильева',
        'address': 'Новиградский проспект, 16',
        'metroStation': 8,
        'phone': '+79853473120',
        'rentTime': 3,
        'deliveryDate': '2024-10-20',
        'comment': 'синий забор',
        'color': [
            'GREY'
        ]
    }

    order_data_black_2 = {
        'firstName': 'Петро',
        'lastName': 'Вайнштейн',
        'address': 'Туссент, улица Яблоневая',
        'metroStation': 10,
        'phone': '+76072861439',
        'rentTime': 7,
        'deliveryDate': '2024-10-19',
        'comment': 'не опаздывать',
        'color': [
            'BLACK'
        ]
    }

    order_data_two_colors_3 = {
        'firstName': 'Ксения',
        'lastName': 'Фазеева',
        'address': 'Шалфей и Розмарин',
        'metroStation': 15,
        'phone': '+73457398129',
        'rentTime': 1,
        'deliveryDate': '2024-10-30',
        'comment': 'проверьте исправность',
        'color': [
            'BLACK', 'GREY'
        ]
    }

    order_data_no_colors_4 = {
        'firstName': 'Иван',
        'lastName': 'Корпут',
        'address': 'Замок Цинтры',
        'metroStation': 20,
        'phone': '+79836517357',
        'rentTime': 2,
        'deliveryDate': '2024-10-20',
        'comment': 'безумно можно быть первым',
        'color': []
    }