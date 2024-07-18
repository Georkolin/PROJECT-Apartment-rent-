def handle_rent_out_district_choice(message):
    district = message.text
    bot.reply_to(message, f"Ви обрали район {district}. Дякуємо! Ми допоможемо вам здати квартиру.")
