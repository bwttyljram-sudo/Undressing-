import datetime
from telebot import TeleBot, types

TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_USERNAME = "@ZenoX_Tools"  # قناة الاشتراك الإجباري

bot = TeleBot(TOKEN, parse_mode="HTML")

# قاعدة بيانات مؤقتة للذاكرة
users_db = {}

# قاموس اللغات لكافة الواجهات والرسائل
TRANSLATIONS = {
    "English": {
        "welcome_back": "Welcome back! 🌟\nThe most powerful AI platform to generate videos and face swaps realistically.",
        "btn_start_app": "Start Using Bot 🤖",
        "btn_balance": "Account Balance 📊",
        "btn_buy": "Buy Credits ⭐",
        "btn_earn": "Earn Free Credits 🪄",
        "btn_lang": "Languages 🌐",
        "msg_lang_select": "Choose your language:👇🏻",
        "msg_start_app": "إضغط على الزر أدناه لإستخدام البوت 👇🏻",
        "btn_open_app": "إبدا إستخدام البوت 🤖",
        "buy_title": "اختر ما تريد شراءه 👇🏻\nستحصل على مزايا دائمة عند شراء أي باقة 🎉\n\n• معالجة فيديو أسرع VIP 🚀\n• إمكانية توليد مقاطع تصل إلى 30 ثانية ⏱️\n• معزز جودة الوجه بدقة أعلى 4 مرات (4K) ✨",
        "pricing_btn": "📋 قائمة أسعار الخدمات بالكامل",
        "btn_back_purchase": "🔙 العودة لقائمة الشراء",
        "btn_back_main": "🔙 العودة للقائمة الرئيسية",
        "btn_share": "📤 مشاركة الرابط مع الأصدقاء",
        "share_promo": "🔥 بوت خلع الملابس بالذكاء الاصطناعي مجاناً! واقعي جداً",
        "check_sub_err": "⚠️ عذراً، يجب عليك الاشتراك في قناة البوت لتتمكن من استخدامه!",
        "btn_sub": "📢 اشترك في القناة أولاً",
        "btn_check_sub": "🔄 تحقق من الاشتراك"
    },
    "العربية": {
        "welcome_back": "أهلاً بك مجدداً! 🌟\nأقوى منصة ذكاء اصطناعي لتوليد الفيديوهات وتبديل الوجوه بواقعية شديدة.",
        "btn_start_app": "بدء إستخدام البوت 🤖",
        "btn_balance": "رصيد الحساب 📊",
        "btn_buy": "شراء رصيد ⭐",
        "btn_earn": "إربح رصيد مجاني 🪄",
        "btn_lang": "الغات 🌐",
        "msg_lang_select": "Choose your language:👇🏻",
        "msg_start_app": "إضغط على الزر أدناه لإستخدام البوت 👇🏻",
        "btn_open_app": "إبدا إستخدام البوت 🤖",
        "buy_title": "اختر ما تريد شراءه 👇🏻\nستحصل على مزايا دائمة عند شراء أي باقة 🎉\n\n• معالجة فيديو أسرع VIP 🚀\n• إمكانية توليد مقاطع تصل إلى 30 ثانية ⏱️\n• معزز جودة الوجه بدقة أعلى 4 مرات (4K) ✨",
        "pricing_btn": "📋 قائمة أسعار الخدمات بالكامل",
        "btn_back_purchase": "🔙 العودة لقائمة الشراء",
        "btn_back_main": "🔙 العودة للقائمة الرئيسية",
        "btn_share": "📤 مشاركة الرابط مع الأصدقاء",
        "share_promo": "🔥 بوت خلع الملابس بالذكاء الاصطناعي مجاناً! واقعي جداً",
        "check_sub_err": "⚠️ عذراً، يجب عليك الاشتراك في قناة البوت لتتمكن من استخدامه!",
        "btn_sub": "📢 اشترك في القناة أولاً",
        "btn_check_sub": "🔄 تحقق من الاشتراك"
    },
    "Russian": {
        "welcome_back": "С возвращением! 🌟\nСамая мощная платформа ИИ для создания видео и замены лиц.",
        "btn_start_app": "Начать бота 🤖",
        "btn_balance": "Баланс 📊",
        "btn_buy": "Купить кредиты ⭐",
        "btn_earn": "Бесплатные кредиты 🪄",
        "btn_lang": "Языки 🌐",
        "msg_lang_select": "Choose your language:👇🏻",
        "msg_start_app": "Нажмите кнопку ниже, чтобы использовать бота 👇🏻",
        "btn_open_app": "Запустить бота 🤖",
        "buy_title": "Выберите, что вы хотите купить 👇🏻",
        "pricing_btn": "📋 Полный прайс-лист услуг",
        "btn_back_purchase": "🔙 Назад к покупкам",
        "btn_back_main": "🔙 В главное меню",
        "btn_share": "📤 Поделиться с друзьями",
        "share_promo": "🔥 Бесплатный ИИ бот!",
        "check_sub_err": "⚠️ Пожалуйста, подпишитесь на канал!",
        "btn_sub": "📢 Подписаться",
        "btn_check_sub": "🔄 Проверить"
    },
    "Spanish": {
        "welcome_back": "¡Bienvenido de nuevo! 🌟\nLa plataforma de IA más potente.",
        "btn_start_app": "Iniciar Bot 🤖",
        "btn_balance": "Saldo 📊",
        "btn_buy": "Comprar Créditos ⭐",
        "btn_earn": "Obtener Gratis 🪄",
        "btn_lang": "Idiomas 🌐",
        "msg_lang_select": "Choose your language:👇🏻",
        "msg_start_app": "Haga clic en el botón de abajo 👇🏻",
        "btn_open_app": "Empezar 🤖",
        "buy_title": "Elige lo que quieres comprar 👇🏻",
        "pricing_btn": "📋 Lista completa de precios",
        "btn_back_purchase": "🔙 Volver a compras",
        "btn_back_main": "🔙 Menú Principal",
        "btn_share": "📤 Compartir enlace",
        "share_promo": "🔥 ¡Bot de IA gratis!",
        "check_sub_err": "⚠️ ¡Por favor suscríbete al canal!",
        "btn_sub": "📢 Suscribirse",
        "btn_check_sub": "🔄 Verificar"
    },
    "Français": {
        "welcome_back": "Bon retour! 🌟\nLa plateforme d'IA la plus puissante.",
        "btn_start_app": "Démarrer Bot 🤖",
        "btn_balance": "Solde 📊",
        "btn_buy": "Acheter Crédits ⭐",
        "btn_earn": "Gagner Gratuit 🪄",
        "btn_lang": "Langues 🌐",
        "msg_lang_select": "Choose your language:👇🏻",
        "msg_start_app": "Cliquez sur le bouton ci-dessous 👇🏻",
        "btn_open_app": "Commencer 🤖",
        "buy_title": "Choisissez ce que vous voulez acheter 👇🏻",
        "pricing_btn": "📋 Liste complète des prix",
        "btn_back_purchase": "🔙 Retour aux achats",
        "btn_back_main": "🔙 Menu Principal",
        "btn_share": "📤 Partager le lien",
        "share_promo": "🔥 Bot IA gratuit!",
        "check_sub_err": "⚠️ Veuillez vous abonner au canal!",
        "btn_sub": "📢 S'abonner",
        "btn_check_sub": "🔄 Vérifier"
    }
}

def get_user_lang(user_id):
    return users_db.get(str(user_id), {}).get("lang", "English")

def check_subscription(user_id):
    if not CHANNEL_USERNAME or CHANNEL_USERNAME == "@YourChannelUsername":
        return True
    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status in ['member', 'creator', 'administrator']:
            return True
    except Exception:
        pass
    return False

# إنشاء لوحة الأزرار الرئيسية أسفل الشات بالتنسيق المطلوب
def get_main_chat_keyboard(lang="English"):
    t = TRANSLATIONS.get(lang, TRANSLATIONS["English"])
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    btn1 = types.KeyboardButton(t["btn_lang"])        # الزر 1
    btn2 = types.KeyboardButton(t["btn_start_app"])   # الزر 2 (عريض بالقمة)
    btn3 = types.KeyboardButton(t["btn_balance"])     # الزر 3
    btn4 = types.KeyboardButton(t["btn_buy"])         # الزر 4
    btn5 = types.KeyboardButton(t["btn_earn"])        # الزر 5
    
    # الترتيب:
    # الزر 2 عريض بالقمة
    # الزر 4 يمين | الزر 3 يسار
    # الزر 5 يمين | الزر 1 يسار
    kb.add(btn2)
    kb.add(btn4, btn3)
    kb.add(btn5, btn1)
    return kb

# قائمة اختيار اللغات
def send_language_selector(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("English 🇺🇸", callback_data="set_lang_English"),
        types.InlineKeyboardButton("العربية 🇾🇪", callback_data="set_lang_العربية"),
        types.InlineKeyboardButton("Russian 🇷🇺", callback_data="set_lang_Russian"),
        types.InlineKeyboardButton("Spanish 🇪🇸", callback_data="set_lang_Spanish"),
        types.InlineKeyboardButton("Français 🇫🇷", callback_data="set_lang_Français")
    )
    bot.send_message(chat_id, "Choose your language:👇🏻", reply_markup=markup)

# /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = str(message.from_user.id)
    args = message.text.split()
    
    # الإحالة
    if len(args) > 1 and args[1].startswith("ref_"):
        referrer_id = args[1].replace("ref_", "")
        if referrer_id != user_id and user_id not in users_db:
            users_db[user_id] = {
                "lang": "English",
                "perm_balance": 20,
                "ref_balance": 0,
                "refs_count": 0,
                "referred_by": referrer_id
            }
            if referrer_id in users_db:
                users_db[referrer_id]["ref_balance"] += 10
                users_db[referrer_id]["refs_count"] += 1
                try:
                    name = message.from_user.first_name or "مستخدم جديد"
                    bot.send_message(
                        int(referrer_id),
                        f"هنيأ لك قام <b>{name}</b> بالإنضمام عبر رابط الدعوة الخاص بك وقد حصلت على 10 رصيد 🎉"
                    )
                except Exception:
                    pass

    is_new = user_id not in users_db
    if is_new:
        users_db[user_id] = {
            "lang": "English",
            "perm_balance": 20,
            "ref_balance": 0,
            "refs_count": 0
        }
        send_language_selector(message.chat.id)
    else:
        lang = get_user_lang(user_id)
        t = TRANSLATIONS.get(lang, TRANSLATIONS["English"])
        bot.send_message(
            message.chat.id,
            t["welcome_back"],
            reply_markup=get_main_chat_keyboard(lang)
        )

# معالجة تفاعلات القوائم والتغيير
@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
    user_id = str(call.from_user.id)
    lang = get_user_lang(user_id)
    t = TRANSLATIONS.get(lang, TRANSLATIONS["English"])

    if call.data.startswith("set_lang_"):
        selected_lang = call.data.replace("set_lang_", "")
        if user_id not in users_db:
            users_db[user_id] = {"perm_balance": 20, "ref_balance": 0, "refs_count": 0}
        users_db[user_id]["lang"] = selected_lang
        
        # حذف قائمة اللغات وإرسال الرسالة رقم [2] والأزرار في الشات
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception:
            pass
            
        kb = get_main_chat_keyboard(selected_lang)
        bot.send_message(call.message.chat.id, "إضغط على الزر أدناه لإستخدام البوت 👇🏻", reply_markup=kb)
        
        # زر التطبيق المصغر Mini App
        app_markup = types.InlineKeyboardMarkup()
        app_markup.add(types.InlineKeyboardButton("إبدا إستخدام البوت 🤖", web_app=types.WebAppInfo(url="https://your-mini-app-url.com")))
        bot.send_message(call.message.chat.id, "إضغط على الزر أدناه لإستخدام البوت 👇🏻", reply_markup=app_markup)

    elif call.data == "services_pricing":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔙 العودة لقائمة الشراء", callback_data="show_buy_menu"))
        text = (
            "📋 جدول أسعار الخدمات بالنقاط (Credits):\n\n"
            "🎬 توليد مقاطع الفيديو (صورة إلى فيديو):\n"
            "• قاعدة الحساب: 1 ثانية = 1 رصيد\n"
            "• فيديو 10 ثوانٍ = 10 نقاط\n"
            "• فيديو 15 ثانية = 15 نقطة\n"
            "• فيديو 30 ثانية = 30 نقطة (للمشتركين)\n\n"
            "🎭 خدمات الوجوه والتعديل:\n"
            "• تبديل الوجوه في الصور 🖼️: 2 رصيد\n"
            "• تعديل/إزالة الملابس 👙✂️: 4 رصيد\n"
            "• تبديل الوجوه في الفيديو 🎬: 10 رصيد"
        )
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "show_buy_menu":
        show_buy_message(call.message.chat.id, call.message.message_id)

    elif call.data == "main_menu_inline":
        bot.delete_message(call.message.chat.id, call.message.message_id)

def show_buy_message(chat_id, message_id=None):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("📋 قائمة أسعار الخدمات بالكامل", callback_data="services_pricing"),
        types.InlineKeyboardButton("شراء 150 نقطة: 200⭐ (≈ $2.6) 💳", callback_data="pay_150"),
        types.InlineKeyboardButton("شراء 350 نقطة: 400⭐ (≈ $5.2) [وفر 20%] 💳", callback_data="pay_350"),
        types.InlineKeyboardButton("شراء 650 نقطة: 650⭐ (≈ $8.4) [وفر 35%] 💳", callback_data="pay_650"),
        types.InlineKeyboardButton("شراء 1000 نقطة: 950⭐ (≈ $950) [وفر 50%] 🔥", callback_data="pay_1000")
    )
    text = (
        "اختر ما تريد شراءه 👇🏻\n"
        "ستحصل على مزايا دائمة عند شراء أي باقة 🎉\n\n"
        "• معالجة فيديو أسرع VIP 🚀\n"
        "• إمكانية توليد مقاطع تصل إلى 30 ثانية ⏱️\n"
        "• معزز جودة الوجه بدقة أعلى 4 مرات (4K) ✨"
    )
    if message_id:
        bot.edit_message_text(text, chat_id, message_id, reply_markup=markup)
    else:
        bot.send_message(chat_id, text, reply_markup=markup)

# معالجة الضغط على أزرار الشات الحية (Text Handler)
@bot.message_handler(func=lambda message: True)
def handle_chat_buttons(message):
    user_id = str(message.from_user.id)
    text = message.text
    lang = get_user_lang(user_id)
    t = TRANSLATIONS.get(lang, TRANSLATIONS["English"])

    # الزر (1) اللغات 🌐
    if text in [t["btn_lang"], "الغات 🌐", "Languages 🌐"]:
        send_language_selector(message.chat.id)

    # الزر (2) بدء إستخدام البوت 🤖
    elif text in [t["btn_start_app"], "بدء إستخدام البوت 🤖"]:
        app_markup = types.InlineKeyboardMarkup()
        app_markup.add(types.InlineKeyboardButton("إبدا إستخدام البوت 🤖", web_app=types.WebAppInfo(url="https://your-mini-app-url.com")))
        bot.send_message(message.chat.id, "إضغط على الزر أدناه لإستخدام البوت 👇🏻", reply_markup=app_markup)

    # الزر (3) رصيد الحساب 📊
    elif text in [t["btn_balance"], "رصيد الحساب 📊"]:
        u = users_db.get(user_id, {"perm_balance": 20, "ref_balance": 0})
        perm = u.get("perm_balance", 20)
        ref = u.get("ref_balance", 0)
        total = perm + ref
        
        now_str = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S GMT")
        msg = (
            f"{now_str}\n\n"
            f"رصيدك الدائم {perm} نقطة 📊\n"
            f"رصيد الدعوات {ref} نقطة 🔗\n\n"
            f"إجمالي الرصيد القابل للإستخدام {total} نقطة 🟢\n\n"
            f"الـ ID الخاص بحسابك {user_id}\n\n\n"
            f"‼️ ملاحضة أقدم رصيد للدعوات تنتهي صلاحيتة\n"
            f"بعد 14 يوم إذا لم يتم إستخدامة... الرصيد الدائم\n"
            f"صالح مدى الحياة 💥"
        )
        bot.send_message(message.chat.id, msg)

    # الزر (4) شراء رصيد ⭐
    elif text in [t["btn_buy"], "شراء رصيد ⭐"]:
        show_buy_message(message.chat.id)

    # الزر (5) إربح رصيد مجاني 🪄
    elif text in [t["btn_earn"], "إربح رصيد مجاني 🪄"]:
        u = users_db.get(user_id, {"ref_balance": 0, "refs_count": 0})
        bot_info = bot.get_me()
        bot_username = bot_info.username if bot_info else "YourBotName"
        ref_link = f"https://t.me/{bot_username}?start={user_id}"
        
        msg = (
            "🪄 اكسب رصيداً مجانياً ودائماً!\n\n"
            "شارك رابطك الخاص مع أصدقائك، واحصل على:\n"
            "🎁 10 نقاط مجانية لكل صديق ينضم عبر رابطك\n\n\n"
            "🔗 رابط الدعوة الخاص بك (انسخه أو شاركه مباشرة):\n"
            f"{ref_link}\n\n\n"
            "📊 إحصائياتك:\n"
            f"• عدد الدعوات الناجحة: {u.get('refs_count', 0)} أصدقاء 👥\n"
            f"• إجمالي الرصيد المكتسب: {u.get('ref_balance', 0)} نقطة 🟢\n\n\n"
            "‼️ ملاحظة: يتم احتساب الرصيد تلقائياً فور انضمام\n"
            "صديقك للبوت، وستصلك رسالة تهنئة فورية.\n"
            "رصيد الدعوات صالح لمدة 30 يوماً."
        )
        
        promo_text = "🔥 بوت خلع الملابس بالذكاء الاصطناعي مجاناً! واقعي جداً"
        share_url = f"https://t.me/share/url?url={ref_link}&text={promo_text}"
        
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("📤 مشاركة الرابط مع الأصدقاء", url=share_url),
            types.InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="main_menu_inline")
        )
        bot.send_message(message.chat.id, msg, reply_markup=markup)

if __name__ == "__main__":
    print("🤖 Bot is successfully running...")
    bot.infinity_polling()
