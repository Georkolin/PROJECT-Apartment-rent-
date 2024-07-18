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
