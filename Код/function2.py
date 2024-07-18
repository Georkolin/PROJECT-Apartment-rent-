@bot.message_handler(commands=['start'])
def send_welcome(message):
    options = ["Орендувати квартиру", "Здати в оренду"]
    bot.reply_to(message, "Привіт, я твій найкращий помічник бот-рієлтор! Що саме бажаєш обрати?", reply_markup=generate_keyboard(options))
    bot.register_next_step_handler(message, handle_main_choice)