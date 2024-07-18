def handle_district_choice(message):
    district = message.text
    bot.reply_to(message, f"Ви обрали район {district}. Що саме вас цікавить?")
