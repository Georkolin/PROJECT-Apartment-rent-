def handle_rent_out_price_choice(message, chosen_district):
    # Отримуємо текст повідомлення, яке містить введену користувачем ціну
    chosen_price = message.text
    
    try:
        # Пробуємо конвертувати введену ціну у тип float
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
#функція забезпечує перевірку правильності введеної ціни і переходить до наступного етапу — вибору кількості кімнат.