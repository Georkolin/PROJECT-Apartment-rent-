def handle_floor_choice(message, chosen_district, chosen_price, chosen_room):
    chosen_floor = message.text
    floor_filters = [str(i) for i in range(1, 31)]
    if chosen_floor in floor_filters:
        bot.reply_to(message, f"Ви обрали квартиру на {chosen_floor} поверсі. Обробка запиту...")

        price_range = chosen_price.split(' - ')
        price_min_str = price_range[0].replace(' ', '').replace(',', '')
        price_max_str = price_range[1].replace(' ', '').replace(',', '')

        price_min = float(price_min_str)
        price_max = float(price_max_str)

        matching_flats = []
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                flat_price = float(row[1]) 

                if (row[0] == chosen_district or (flat_price >= price_min and flat_price <= price_max)) and row[2] == chosen_room and row[3] == chosen_floor:
                    matching_flats.append(row)

        if matching_flats:
            for flat in matching_flats:
                bot.send_message(message.chat.id, f"Район: {flat[0]}, Ціна: {flat[1]}, Кількість кімнат: {flat[2]}, Поверх: {flat[3]}")
        else:
            bot.send_message(message.chat.id, "Нажаль, немає квартир, які відповідають вашим умовам.")
            
            options = ["Шукати інші варіанти", "Шукати схожі квартири"]
            bot.send_message(message.chat.id, "Що бажаєте зробити далі?", reply_markup=generate_keyboard(options))
            bot.register_next_step_handler(message, handle_no_flats_choice, chosen_district, chosen_price, chosen_room)

    else:
        bot.reply_to(message, "Будь ласка, оберіть один із запропонованих поверхів.")
        bot.register_next_step_handler(message, handle_floor_choice, chosen_district, chosen_price, chosen_room)
