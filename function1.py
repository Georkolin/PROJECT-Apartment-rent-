def generate_keyboard(options, row_width=2):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for i in range(0, len(options), row_width):
        markup.row(*[types.KeyboardButton(option) for option in options[i:i + row_width]])
    return markup
