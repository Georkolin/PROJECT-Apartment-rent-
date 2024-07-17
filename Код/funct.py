import csv

csv_file_path = 'rent_out_data.csv'  # шлях до CSV файлу

def handle_rent_out_floor_choice(message, chosen_district, chosen_price, chosen_room):
  
    
    # Створюємо список можливих варіантів поверхів (від 1 до 30)
    floor_filters = [str(i) for i in range(1, 31)]
    if chosen_floor in floor_filters:
        bot.reply_to(message, f"Ви обрали квартиру на {chosen_floor} поверсі. Дані збережено.")
        with open(csv_file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([chosen_district, chosen_price, chosen_room, chosen_floor])
        bot.reply_to(message, "Ваші дані успішно збережено.")
        bot.send_message(message.chat.id, "Дякуємо за використання наших послуг! Ваші дані були успішно збережені.")
    else:
        bot.reply_to(message, "Будь ласка, оберіть один із запропонованих поверхів.")
        
        # Реєструємо поточний обробник як наступний крок, щоб користувач міг повторити вибір поверху
        bot.register_next_step_handler(message, handle_rent_out_floor_choice, chosen_district, chosen_price, chosen_room)
   # функція забезпечує перевірку правильності вибору поверху, збереження зібраних даних у CSV файл та повідомлення користувача про успішне збереження даних.