def ask_for_district(message, prompt):
    bot.reply_to(message, prompt, reply_markup=generate_keyboard(districts))
