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
