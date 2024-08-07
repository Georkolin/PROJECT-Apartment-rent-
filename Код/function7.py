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
