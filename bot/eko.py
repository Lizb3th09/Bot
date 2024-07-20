#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import (
    ForceReply, 
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    )
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hola {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    
    #Respuesta de los botones
    
    if query.data == "Credencial":
        
        credencial = [
            [InlineKeyboardButton('Nueva Credencial', callback_data='Nueva_Credencial')],
            [InlineKeyboardButton('Extravío de Credencial', callback_data='Extravío_Credencial')],
        ]
        await query.edit_message_text(text="Seleccionaste Credencial. ¿Qué quieres hacer?", reply_markup=InlineKeyboardMarkup(credencial))        
    
    elif query.data == 'Nueva_Credencial':
        await query.edit_message_text(text="Aquí tienes el formulario para una nueva credencial. https://docs.google.com/forms/d/e/1FAIpQLSc_C-74SkgvzJvdmu72Vec-DaH6MMzfyhr2_27OfKqv1B5dng/viewform")
    elif "Constancia" in query.data:
        await query.edit_message_text(text="Manda correo a escolares@ite.edu.mx para solicitar tu constancia de estudios")
    elif "Titulo" in query.data:
        await query.edit_message_text(text="Estos son los documentos que se necesitan para la Titulacion")
    elif "Departamentos" in query.data:
        await query.edit_message_text(text="Te muestro el mapa de donde esta cada oficina y en que edificio se encuentra")
    elif "Seguro social" in query.data:
        await query.edit_message_text(text="Necesitas los siguiemtes documentos")
    #await query.edit_message_text(text=f"Selected option: {query.data}")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    #mensaje = update.message.text
    

# Respuestas si el usuario escribe las opciones

    if update.message.text == 'Credencial':
        credencial = "Aquí tienes el formulario para la credencial https://docs.google.com/forms/d/e/1FAIpQLSc_C-74SkgvzJvdmu72Vec-DaH6MMzfyhr2_27OfKqv1B5dng/viewform"
        await update.message.reply_text(credencial)
    
    if update.message.text == 'Constancia':
        constancia = "Manda correo a escolares@ite.edu.mx para solicitar tu constancia de estudios"
        await update.message.reply_text(constancia)
    
    if update.message.text == 'Titulo':
        titulo = "Estos son los documentos que se necesitan para la Titulacion"
        await update.message.reply_text(titulo)
    
    if update.message.text == 'Departamentos':
        departamento = "Te muestro el mapa de donde esta cada oficina y en que edificio se encuentra"
        await update.message.reply_text(departamento)
    
    if update.message.text == 'Seguro social':
        seguro = "Necesitas los siguiemtes documentos"
        await update.message.reply_text(seguro)
    
    
    if update.message.text == 'Hola':
        saludo = "Como puedo ayudarte hoy 😁"
        await update.message.reply_text(saludo)
    
    if update.message.text == '😊':
        
        # Botones de  las opciones
        
        keyboard = [[InlineKeyboardButton('Credencial', callback_data='Credencial')], 
            [InlineKeyboardButton('Constancia', callback_data='Constancia')],
            [InlineKeyboardButton('Titulo', callback_data='Titulo')],
            [InlineKeyboardButton('Departamentos', callback_data='Departamentos'),
           ], [InlineKeyboardButton('Seguro social', callback_data='Seguro social'),
           ]]
        
        menu_choices = InlineKeyboardMarkup(keyboard)
        
        
# Send the message with menu
        await context.bot.send_message(
    chat_id=update.message.chat_id, text="Menu de Opciones", reply_markup=menu_choices)
        return 

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("7012511703:AAEYbYjC0Amo2nKR_F4uNO16nayMkv9inh4").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(CallbackQueryHandler(button))
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
