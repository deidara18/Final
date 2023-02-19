import telebot
from telebot import types


bot = telebot.TeleBot("6200671469:AAGf4Q_BXc6YseKa5JkPXQ1aE1B_XyoF-o8")


# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("Привет")
#     btn2 = types.KeyboardButton("Гайды")
#     markup.add(btn1, btn2)
#     bot.send_message(message.chat.id,
#                      "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user),
#                      reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, text="Привет, выбирай гайд!)")
    if message.text == "Гайды":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        cryo = types.KeyboardButton("Лед")
        pyro = types.KeyboardButton("Огонь")
        anemo = types.KeyboardButton("Ветер")
        dendro = types.KeyboardButton("Дендро")
        electro = types.KeyboardButton("Электро")
        water = types.KeyboardButton("Вода")
        geo = types.KeyboardButton("Гео")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(cryo, pyro, anemo, dendro, electro, water, geo, back)
        bot.send_message(message.chat.id, text="Выбери стихию, а потом песронажа", reply_markup=markup)

    if message.text == "Лед":
        markup = types.InlineKeyboardMarkup(row_width=3)
        laila = types.InlineKeyboardButton(text='Лайла', callback_data="0", url='https://genshin-info.ru/wiki/personazhi/layla/')
        shenkhe = types.InlineKeyboardButton(text="Шэнь Хэ",callback_data="1", url='https://genshin-info.ru/wiki/personazhi/shen-khe/')
        mika = types.InlineKeyboardButton(text='Мика', callback_data='2', url='https://genshin-info.ru/wiki/personazhi/mika/')
        eloi = types.InlineKeyboardButton(text='Элой', callback_data='3', url='https://genshin-info.ru/wiki/personazhi/eloy/')
        ayaka = types.InlineKeyboardButton(text='Аяка', callback_data='4', url='https://genshin-info.ru/wiki/personazhi/ayaka/')
        eola = types.InlineKeyboardButton(text='Эола', callback_data='5', url='https://genshin-info.ru/wiki/personazhi/eola/')
        rosaria = types.InlineKeyboardButton(text='Розария', callback_data='6', url='https://genshin-info.ru/wiki/personazhi/rosaria/')
        ganyu = types.InlineKeyboardButton(text='Гань Юй', callback_data='7', url='https://genshin-info.ru/wiki/personazhi/ganyu/')
        diona = types.InlineKeyboardButton(text='Диона', callback_data='8', url='https://genshin-info.ru/wiki/personazhi/diona/')
        qiqi = types.InlineKeyboardButton(text='Ци Ци', callback_data='9', url='https://genshin-info.ru/wiki/personazhi/qiqi/')
        chongyun = types.InlineKeyboardButton(text='Чун Юнь', callback_data='10', url='https://genshin-info.ru/wiki/personazhi/chongyun/')
        kaeya = types.InlineKeyboardButton(text='Кэйа', callback_data='11', url='https://genshin-info.ru/wiki/personazhi/kaeya/')

        markup.add(laila, shenkhe, mika, eloi, ayaka, eola, rosaria, ganyu, diona, qiqi, chongyun, kaeya)
        bot.send_message(message.chat.id, text="Выбери персонажа стихии Лед", reply_markup=markup)

    if message.text == "Огонь":
        markup = types.InlineKeyboardMarkup(row_width=3)
        dekhya = types.InlineKeyboardButton(text='Дэхья', callback_data='10', url='https://genshin-info.ru/wiki/personazhi/dekhya/')
        toma = types.InlineKeyboardButton(text='Тома', callback_data="0", url='https://genshin-info.ru/wiki/personazhi/toma/?bxrand=1676758092587')
        yeimiya = types.InlineKeyboardButton(text='Ёимия', callback_data="1", url='https://genshin-info.ru/wiki/personazhi/yeimiya/')
        yan_fey = types.InlineKeyboardButton(text='Янь Фэй', callback_data="2", url='https://genshin-info.ru/wiki/personazhi/yan-fey/')
        hu_tao = types.InlineKeyboardButton(text='Ху Тао', callback_data="3", url='https://genshin-info.ru/wiki/personazhi/hu-tao/')
        xinyan = types.InlineKeyboardButton(text='Синь Янь', callback_data="4", url='https://genshin-info.ru/wiki/personazhi/xinyan/')
        klee = types.InlineKeyboardButton(text='Кли', callback_data="5", url='https://genshin-info.ru/wiki/personazhi/klee/')
        diluc = types.InlineKeyboardButton(text='Дилюк', callback_data='6', url='https://genshin-info.ru/wiki/personazhi/diluc/')
        amber = types.InlineKeyboardButton(text='Эмбер', callback_data='7', url='https://genshin-info.ru/wiki/personazhi/amber/')
        xiangling = types.InlineKeyboardButton(text='Сян Лин', callback_data='8', url='https://genshin-info.ru/wiki/personazhi/xiangling/')
        bennett = types.InlineKeyboardButton(text='Беннет', callback_data='9', url='https://genshin-info.ru/wiki/personazhi/bennett/')

        markup.add(toma, yeimiya, yan_fey, hu_tao, xinyan, klee, diluc, amber, xiangling, bennett)
        bot.send_message(message.chat.id, text="Выбери персонажа стихии Огонь", reply_markup=markup)

    if message.text == "Ветер":
        markup = types.InlineKeyboardMarkup(row_width=3)
        strannik = types.InlineKeyboardButton(text='Странник', callback_data='0', url='https://genshin-info.ru/wiki/personazhi/strannik/')
        faruzan = types.InlineKeyboardButton(text='Фарузан', callback_data='1', url='https://genshin-info.ru/wiki/personazhi/faruzan/')
        kheydzo = types.InlineKeyboardButton(text='Хэйдзо', callback_data='2', url='https://genshin-info.ru/wiki/personazhi/kheydzo/')
        sayu = types.InlineKeyboardButton(text='Саю', callback_data='3', url='https://genshin-info.ru/wiki/personazhi/sayu/')
        kadzukha = types.InlineKeyboardButton(text='Кадзуха', callback_data='4', url='https://genshin-info.ru/wiki/personazhi/kadzukha/')
        xiao = types.InlineKeyboardButton(text='Сяо', callback_data='5', url='https://genshin-info.ru/wiki/personazhi/xiao/')
        venti = types.InlineKeyboardButton(text='Венти', callback_data='6', url='https://genshin-info.ru/wiki/personazhi/venti/')
        jean = types.InlineKeyboardButton(text='Джинн', callback_data='7', url='https://genshin-info.ru/wiki/personazhi/jean/')
        sucrose = types.InlineKeyboardButton(text='Сахароза', callback_data='8', url='https://genshin-info.ru/wiki/personazhi/sucrose/')

        markup.add(strannik, faruzan, kheydzo, sayu, kadzukha, xiao, venti, jean, sucrose)
        bot.send_message(message.chat.id, text="Выбери персонажа стихии Ветер", reply_markup=markup)

    if message.text == "Дендро":
        markup = types.InlineKeyboardMarkup(row_width=3)
        al_khaytam = types.InlineKeyboardButton(text='Аль-Хайтам', callback_data='0', url='https://genshin-info.ru/wiki/personazhi/al-khaytam/')
        yao_yao = types.InlineKeyboardButton(text='Яо Яо', callback_data='1', url='https://genshin-info.ru/wiki/personazhi/yao-yao/')
        nakhida = types.InlineKeyboardButton(text='Нахида', callback_data='2', url='https://genshin-info.ru/wiki/personazhi/nakhida/')
        tignari = types.InlineKeyboardButton(text='Тигнари', callback_data='3', url='https://genshin-info.ru/wiki/personazhi/tignari/')
        kollei = types.InlineKeyboardButton(text='Коллеи', callback_data='4', url='https://genshin-info.ru/wiki/personazhi/kollei/')

        markup.add(al_khaytam, yao_yao, nakhida, tignari, kollei)
        bot.send_message(message.chat.id, text="Выбери персонажа стихии Дендро", reply_markup=markup)

    if message.text == "Электро":
        markup = types.InlineKeyboardMarkup(row_width=3)
        sayno = types.InlineKeyboardButton(text='Сайно', callback_data='0', url='https://genshin-info.ru/wiki/personazhi/sayno/')
        dori = types.InlineKeyboardButton(text='Дори', callback_data='1', url='https://genshin-info.ru/wiki/personazhi/dori/')
        kuki = types.InlineKeyboardButton(text='Синобу', callback_data='2', url='https://genshin-info.ru/wiki/personazhi/kuki/')
        yae_miko = types.InlineKeyboardButton(text='Яэ Мико', callback_data='3', url='https://genshin-info.ru/wiki/personazhi/yae-miko/')
        rayden = types.InlineKeyboardButton(text='Райдэн', callback_data='4', url='https://genshin-info.ru/wiki/personazhi/rayden/')
        sara = types.InlineKeyboardButton(text='Сара', callback_data='5', url='https://genshin-info.ru/wiki/personazhi/sara/')
        keqing = types.InlineKeyboardButton(text='Кэ Цин', callback_data='6', url='https://genshin-info.ru/wiki/personazhi/keqing/')
        fischl = types.InlineKeyboardButton(text='Фишль', callback_data='7', url='https://genshin-info.ru/wiki/personazhi/fischl/')
        razor = types.InlineKeyboardButton(text='Рэйзор', callback_data='8', url='https://genshin-info.ru/wiki/personazhi/razor/')
        lisa = types.InlineKeyboardButton(text='Лиза', callback_data='9', url='https://genshin-info.ru/wiki/personazhi/lisa/')
        beidou = types.InlineKeyboardButton(text='Бэй Доу', callback_data='10',  url='https://genshin-info.ru/wiki/personazhi/beidou/')

        markup.add(sayno, dori, kuki, yae_miko, rayden, sara, keqing, fischl, razor, lisa, beidou)
        bot.send_message(message.chat.id, text="Выбери персонажа стихии Электро", reply_markup=markup)

    if message.text == "Вода":
        markup = types.InlineKeyboardMarkup(row_width=3)
        nilu = types.InlineKeyboardButton(text='Нилу', callback_data='0', url='https://genshin-info.ru/wiki/personazhi/nilu/')
        kandakiya = types.InlineKeyboardButton(text='Кандакия', callback_data='1', url='https://genshin-info.ru/wiki/personazhi/kandakiya/')
        e_lan = types.InlineKeyboardButton(text='Е Лань', callback_data='2', url='https://genshin-info.ru/wiki/personazhi/e-lan/')
        ayato = types.InlineKeyboardButton(text='Аято', callback_data='3', url='https://genshin-info.ru/wiki/personazhi/ayato/')
        kokomi = types.InlineKeyboardButton(text='Кокоми', callback_data='4', url='https://genshin-info.ru/wiki/personazhi/kokomi/')
        tartaglia = types.InlineKeyboardButton(text='Тарталья', callback_data='5', url='https://genshin-info.ru/wiki/personazhi/tartaglia/')
        mona = types.InlineKeyboardButton(text='Мона', callback_data='6', url='https://genshin-info.ru/wiki/personazhi/mona/')
        xingqiu = types.InlineKeyboardButton(text='Син Цю', callback_data='7', url='https://genshin-info.ru/wiki/personazhi/xingqiu/')
        barbara = types.InlineKeyboardButton(text='Барбара', callback_data='8', url='https://genshin-info.ru/wiki/personazhi/barbara/')

        markup.add(nilu, kandakiya, e_lan, ayato, kokomi, tartaglia, mona, xingqiu, barbara)
        bot.send_message(message.chat.id, text="Выбери персонажа стихии Вода", reply_markup=markup)

    if message.text == "Гео":
        markup = types.InlineKeyboardMarkup(row_width=3)
        yun_tszin = types.InlineKeyboardButton(text='Юнь Цзинь', callback_data='0', url='https://genshin-info.ru/wiki/personazhi/yun-tszin/')
        itto = types.InlineKeyboardButton(text='Итто', callback_data='1', url='https://genshin-info.ru/wiki/personazhi/itto/')
        goro = types.InlineKeyboardButton(text='Горо', callback_data='2', url='https://genshin-info.ru/wiki/personazhi/goro/')
        albedo = types.InlineKeyboardButton(text='Альбедо', callback_data='3', url='https://genshin-info.ru/wiki/personazhi/albedo/')
        zhongli = types.InlineKeyboardButton(text='Чжун Ли', callback_data='4', url='https://genshin-info.ru/wiki/personazhi/zhongli/')
        noelle = types.InlineKeyboardButton(text='Ноэлль', callback_data='5', url='https://genshin-info.ru/wiki/personazhi/noelle/')
        ningguang = types.InlineKeyboardButton(text='Нин Гуан', callback_data='6', url='https://genshin-info.ru/wiki/personazhi/ningguang/')

        markup.add(yun_tszin, itto, goro, albedo, zhongli, noelle, ningguang)
        bot.send_message(message.chat.id, text="Выбери персонажа стихии Гео", reply_markup=markup)

    if message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Показать гайды на персонажей ")

    if message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Привет")
        btn2 = types.KeyboardButton("Гайды")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)


bot.polling(none_stop=True)
