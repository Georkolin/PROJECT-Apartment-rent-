def handle_main_choice(message):
    choice = message.text
    if choice == "Орендувати квартиру":
        ask_for_district(message, "Я допоможу орендувати квартиру в Києві. Оберіть район:")
        bot.register_next_step_handler(message, handle_district_choice)
    elif choice == "Здати в оренду":
        ask_for_district(message, "Зараз ми допоможемо вам здати квартиру в оренду. Оберіть район:")
        bot.register_next_step_handler(message, handle_rent_out_district_choice)
    else:
        bot.reply_to(message, "Будь ласка, оберіть один із запропонованих варіантів.")
        bot.register_next_step_handler(message, handle_main_choice)
