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