class Data:
    # Данные для создания курьера
    valid_login = "ninja"
    valid_password = "1234"
    valid_firstName = "saske"
    
    valid_courier_data = {
        'login': valid_login,
        'password': valid_password,
        'firstName': valid_firstName
    }
    
    # Сообщения об ошибках
    class Messages:
        LOGIN_ALREADY_EXISTS = "Этот логин уже используется. Попробуйте другой."
        NOT_ENOUGH_DATA_FOR_CREATE = "Недостаточно данных для создания учетной записи"
        ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
        NOT_ENOUGH_DATA_FOR_LOGIN = "Недостаточно данных для входа"
        ORDER_NOT_FOUND = "Заказ не найден"
    
    # Данные для создания заказа
    order_data_grey_1 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["GREY"]
    }
    
    order_data_black_2 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }
    
    order_data_two_colors_3 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK", "GREY"]
    }
    
    order_data_no_colors_4 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": []
    }