def handle_rent_out_district_choice(message):
    # Отримуємо текст повідомлення, яке містить вибраний користувачем район
    chosen_district = message.text
    
    # Перевіряємо, чи є вибраний район у списку районів
    if chosen_district in districts:
        # Відповідаємо користувачу, що район обрано, і запитуємо ввести ціну
        bot.reply_to(message, f"Ви обрали район {chosen_district}. Введіть, будь ласка, ціну (наприклад, 6700.00):")
        bot.register_next_step_handler(message, handle_rent_out_price_choice, chosen_district)
    else:
        bot.reply_to(message, "Будь ласка, оберіть один із запропонованих районів.")
        bot.register_next_step_handler(message, handle_rent_out_district_choice)
# Таким чином, функція забезпечує взаємодію з користувачем для вибору району та переходу до введення ціни, або повертає його до вибору району, якщо вибір був неправильний.