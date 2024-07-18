import telebot
from telebot import types
import csv

bot = telebot.TeleBot('7355214931:AAF7afKv7D33sOmMF5WOhhwQ0OhUVBp-upk')

csv_file_path = 'FLATS.csv'

with open('district.csv', 'r') as file:
    reader = csv.reader(file)
    districts = next(reader)

def generate_keyboard(options, row_width=2):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for i in range(0, len(options), row_width):
        markup.row(*[types.KeyboardButton(option) for option in options[i:i + row_width]])
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    options = ["Орендувати квартиру", "Здати в оренду"]
    bot.reply_to(message, "Привіт, я твій найкращий помічник бот-рієлтор! Що саме бажаєш обрати?", reply_markup=generate_keyboard(options))
    bot.register_next_step_handler(message, handle_main_choice)

def handle_main_choice(message):
    choice = message.text
    if choice == "Орендувати квартиру":
        bot.reply_to(message, "Я допоможу орендувати квартиру в Києві. Оберіть район:", reply_markup=generate_keyboard(districts))
        bot.register_next_step_handler(message, handle_district_choice)
    elif choice == "Здати в оренду":
        bot.reply_to(message, "Зараз ми допоможемо вам здати квартиру в оренду. Оберіть район:", reply_markup=generate_keyboard(districts))
        bot.register_next_step_handler(message, handle_rent_out_district_choice)
    else:
        bot.reply_to(message, "Будь ласка, оберіть один із запропонованих варіантів.")
        bot.register_next_step_handler(message, handle_main_choice)

def handle_rent_out_district_choice(message):
    chosen_district = message.text
    if chosen_district in districts:
        bot.reply_to(message, f"Ви обрали район {chosen_district}. Введіть, будь ласка, ціну (наприклад, 6700.00):")
        bot.register_next_step_handler(message, handle_rent_out_price_choice, chosen_district)
    else:
        bot.reply_to(message, "Будь ласка, оберіть один із запропонованих районів.")
        bot.register_next_step_handler(message, handle_rent_out_district_choice)

def handle_rent_out_price_choice(message, chosen_district):
    chosen_price = message.text
    try:
        float(chosen_price)
        room_filters = [
            "One bedroom",
            "Two bedroom",
            "Three bedroom",
            "Four bedroom",
            "Studio apartment"
        ]
        bot.reply_to(message, f"Ви ввели ціну {chosen_price}. Оберіть кількість кімнат:", reply_markup=generate_keyboard(room_filters))
        bot.register_next_step_handler(message, handle_rent_out_room_choice, chosen_district, chosen_price)
    except ValueError:
        bot.reply_to(message, "Неправильний формат введеної ціни. Будь ласка, введіть ціну у форматі '6700.00'.")
        bot.register_next_step_handler(message, handle_rent_out_price_choice, chosen_district)

def handle_rent_out_room_choice(message, chosen_district, chosen_price):
    chosen_room = message.text
    room_filters = [
        "One bedroom",
        "Two bedroom",
        "Three bedroom",
        "Four bedroom",
        "Studio apartment"
    ]
    if chosen_room in room_filters:
        floor_filters = [str(i) for i in range(1, 31)]
        bot.reply_to(message, f"Ви обрали {chosen_room} квартиру. Оберіть поверх:", reply_markup=generate_keyboard(floor_filters, row_width=5))
        bot.register_next_step_handler(message, handle_rent_out_floor_choice, chosen_district, chosen_price, chosen_room)
    else:
        bot.reply_to(message, "Будь ласка, оберіть одну з запропонованих категорій.")
        bot.register_next_step_handler(message, handle_rent_out_room_choice, chosen_district, chosen_price)

def handle_rent_out_floor_choice(message, chosen_district, chosen_price, chosen_room):
    chosen_floor = message.text
    floor_filters = [str(i) for i in range(1, 31)]
    if chosen_floor in floor_filters:
        bot.reply_to(message, f"Ви обрали квартиру на {chosen_floor} поверсі. Дані збережено.")
        
        # Збереження даних у CSV файл
        with open(csv_file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([chosen_district, chosen_price, chosen_room, chosen_floor])
        
        bot.reply_to(message, "Ваші дані успішно збережено.")
        bot.send_message(message.chat.id, "Дякуємо за використання наших послуг! Ваші дані були успішно збережені.")
    else:
        bot.reply_to(message, "Будь ласка, оберіть один із запропонованих поверхів.")
        bot.register_next_step_handler(message, handle_rent_out_floor_choice, chosen_district, chosen_price, chosen_room)

def handle_district_choice(message):
    chosen_district = message.text
    price_filters = [
        "5000.00 - 10000.00",
        "10000.00 - 15000.00",
        "15000.00 - 20000.00",
        "20000.00 - 25000.00",
        "25000.00 - 30000.00",
        "30000.00 - 35000.00"
    ]
    if chosen_district in districts:
        bot.reply_to(message, f"Ви обрали район {chosen_district}. Оберіть діапазон цін:", reply_markup=generate_keyboard(price_filters))
        bot.register_next_step_handler(message, handle_price_choice, chosen_district)
    else:
        bot.reply_to(message, "Будь ласка, оберіть один із запропонованих районів.")
        bot.register_next_step_handler(message, handle_district_choice)

def handle_price_choice(message, chosen_district):
    chosen_price = message.text
    price_filters = [
        "5000.00 - 10000.00",
        "10000.00 - 15000.00",
        "15000.00 - 20000.00",
        "20000.00 - 25000.00",
        "25000.00 - 30000.00",
        "30000.00 - 35000.00"
    ]
    if chosen_price in price_filters:
        room_filters = [
            "One bedroom",
            "Two bedroom",
            "Three bedroom",
            "Four bedroom",
            "Studio apartment"
        ]
        bot.reply_to(message, f"Ви вибрали діапазон цін {chosen_price}. Оберіть кількість кімнат:", reply_markup=generate_keyboard(room_filters))
        bot.register_next_step_handler(message, handle_room_choice, chosen_district, chosen_price)
    else:
        bot.reply_to(message, "Будь ласка, оберіть один із запропонованих діапазонів цін.")
        bot.register_next_step_handler(message, handle_price_choice, chosen_district)

def handle_room_choice(message, chosen_district, chosen_price):
    chosen_room = message.text
    room_filters = [
        "One bedroom",
        "Two bedroom",
        "Three bedroom",
        "Four bedroom",
        "Studio apartment"
    ]
    if chosen_room in room_filters:
        floor_filters = [str(i) for i in range(1, 31)]
        bot.reply_to(message, f"Ви обрали {chosen_room} квартиру. Оберіть поверх:", reply_markup=generate_keyboard(floor_filters, row_width=5))
        bot.register_next_step_handler(message, handle_floor_choice, chosen_district, chosen_price, chosen_room)
    else:
        bot.reply_to(message, "Будь ласка, оберіть одну з запропонованих категорій.")
        bot.register_next_step_handler(message, handle_room_choice, chosen_district, chosen_price)

def handle_floor_choice(message, chosen_district, chosen_price, chosen_room):
    chosen_floor = message.text
    floor_filters = [str(i) for i in range(1, 31)]
    if chosen_floor in floor_filters:
        bot.reply_to(message, f"Ви обрали квартиру на {chosen_floor} поверсі. Обробка запиту...")

        # Розбиваємо діапазон цін на мінімальне і максимальне значення
        price_range = chosen_price.split(' - ')
        price_min_str = price_range[0].replace(' ', '').replace(',', '')
        price_max_str = price_range[1].replace(' ', '').replace(',', '')

        price_min = float(price_min_str)
        price_max = float(price_max_str)

        matching_flats = []
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Пропускаємо перший рядок (заголовок)
            for row in reader:
                flat_price = float(row[1])  # Ціна квартири з CSV

                # Перевіряємо, чи ціна квартири потрапляє в обраний діапазон
                if (row[0] == chosen_district or (flat_price >= price_min and flat_price <= price_max)) and row[2] == chosen_room and row[3] == chosen_floor:
                    matching_flats.append(row)

        if matching_flats:
            for flat in matching_flats:
                bot.send_message(message.chat.id, f"Район: {flat[0]}, Ціна: {flat[1]}, Кількість кімнат: {flat[2]}, Поверх: {flat[3]}")
        else:
            bot.send_message(message.chat.id, "Нажаль, немає квартир, які відповідають вашим умовам.")
            # Пропонуємо користувачу варіанти:
            options = ["Шукати інші варіанти", "Шукати схожі квартири"]
            bot.send_message(message.chat.id, "Що бажаєте зробити далі?", reply_markup=generate_keyboard(options))
            bot.register_next_step_handler(message, handle_no_flats_choice, chosen_district, chosen_price, chosen_room)

    else:
        bot.reply_to(message, "Будь ласка, оберіть один із запропонованих поверхів.")
        bot.register_next_step_handler(message, handle_floor_choice, chosen_district, chosen_price, chosen_room)

def handle_no_flats_choice(message, chosen_district, chosen_price, chosen_room):
    choice = message.text
    if choice == "Шукати інші варіанти":
        bot.reply_to(message, "Обирайте інші варіанти", reply_markup=generate_keyboard(districts))
        bot.register_next_step_handler(message, handle_district_choice)
    elif choice == "Шукати схожі квартири":
        bot.reply_to(message, "Оберіть схожі варіанти", reply_markup=generate_keyboard(districts))
        bot.register_next_step_handler(message, handle_district_choice)
    else:
        bot.reply_to(message, "Будь ласка, оберіть один із запропонованих варіантів.")
        bot.register_next_step_handler(message, handle_no_flats_choice, chosen_district, chosen_price, chosen_room)

bot.polling()
