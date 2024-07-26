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
import random
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


# Esta Funcion muestra las imagenes del boton de Departamentos 
async def Mapa(chat_id, context):
    with open("Mapa.png", 'rb') as imagen1:
        await context.bot.send_photo(chat_id=chat_id, photo=imagen1)
    with open("Departamentos.png", 'rb') as imagen2:
        await context.bot.send_photo(chat_id=chat_id, photo=imagen2)

 # Esta Funcion muestra las imagenes del boton de Titulo  
async def Titul(chat_id, context):
    with open("1.png", 'rb') as imagen3:
        await context.bot.send_photo(chat_id=chat_id, photo=imagen3)
    with open("2.png", 'rb') as imagen4:
        await context.bot.send_photo(chat_id=chat_id, photo=imagen4)

    with open("4.jpeg", 'rb') as imagen5:
        await context.bot.send_photo(chat_id=chat_id, photo=imagen5)
    with open("5.jpeg", 'rb') as imagen6:
        await context.bot.send_photo(chat_id=chat_id, photo=imagen6)

# Funcion manda un archivo pdf en el boton Titulo
async def titul(chat_id, context, pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        await context.bot.send_document(chat_id=chat_id, document=pdf_file)

# Funcion que muestra las imagenes del boton de seguro social
async def seguro(chat_id, context):
    with open("alta2.png", 'rb') as imagen7:
        await context.bot.send_photo(chat_id=chat_id, photo=imagen7)
    with open("alta.png", 'rb') as imagen8:
        await context.bot.send_photo(chat_id=chat_id, photo=imagen8)

# Funcion para mandar la imagen del boton inscripcion
async def Inscripcion(chat_id, context):
    with open("Inscripcion.png", 'rb') as imagen9:
        await context.bot.send_photo(chat_id=chat_id, photo=imagen9)
   

# Funcion para mandar las imagenes de actividades complementarias
async def actividades(chat_id, context):
    with open("Ajedres.png", 'rb') as imagen10:
        await context.bot.send_photo(chat_id=chat_id, photo=imagen10)
    with open("Atletismo.png", 'rb') as imagen11:
        await context.bot.send_photo(chat_id=chat_id, photo=imagen11)
    with open("Basquetbol.png", 'rb') as imagen12:
        await context.bot.send_photo(chat_id=chat_id, photo=imagen12)  
    with open("beisbol.png", 'rb') as imagen13:
        await context.bot.send_photo(chat_id=chat_id, photo=imagen13)        
    with open("Escolta.png", 'rb') as imagen14:
        await context.bot.send_photo(chat_id=chat_id, photo=imagen14) 
    with open("Fut femenil.png", 'rb') as imagen15:
        await context.bot.send_photo(chat_id=chat_id, photo=imagen15)    
    with open("Fut varonil.png", 'rb') as imagen16:
        await context.bot.send_photo(chat_id=chat_id, photo=imagen16)   
    with open("Musica.png", 'rb') as imagen17:
        await context.bot.send_photo(chat_id=chat_id, photo=imagen17)
    with open("soft femenil.png", 'rb') as imagen18:
        await context.bot.send_photo(chat_id=chat_id, photo=imagen18) 
           
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
            [InlineKeyboardButton('Extravío de Credencial', callback_data='Extravio_Credencial')],
        ]
        await query.edit_message_text(text="Seleccionaste Credencial. ¿Qué quieres hacer?", reply_markup=InlineKeyboardMarkup(credencial))        
    
    elif query.data == 'Nueva_Credencial':
        await query.edit_message_text(text=" Claro  Para solicitar tu credencial estudiantil  es necesario tomarte una foto, con fondo blanco,cara descubierta (sin lentes,aretes o pirsings ) recordar pasar a escolores en el horario de  lunes a viernes 9:00 a 18:00. Aquí tienes el formulario para solicitar tu credencial por primera vez. https://docs.google.com/forms/d/e/1FAIpQLSc_C-74SkgvzJvdmu72Vec-DaH6MMzfyhr2_27OfKqv1B5dng/viewform")
    
    elif query.data == 'Extravio_Credencial':
        await query.edit_message_text(text="Para Reposicion de la credencial en caso de que se te haya extraviado, mandar un correo a escolares@ite.edu.mx  solicitando la reposicion de tu credencial. Recordar pasar a escolores en el horario de  lunes a viernes 9:00 a 18:00")
    
    elif "Constancia" in query.data:
        await query.edit_message_text(text="Para solicitar una constancia de estudios  mandar una descripcion para que es solicitada a : escolares@ite.edu.mx")
    
    elif "Titulo" in query.data:
        await query.edit_message_text(text="Aquí están los requisitos para solicitar el título y las diferentes Formas para Titularte. Te mostramos los pasos a seguir y Descarga el archivo adjunto.")
        chat_id = update.effective_chat.id
        await Titul(chat_id, context)   
        await titul(chat_id, context,"Requisitos del titulo.pdf")
        
    elif "Seguro social" in query.data:
        await query.edit_message_text(text="Aquí tienes la información con los pasos para dar de alta tu seguro social.")
        chat_id = update.effective_chat.id
        await seguro(chat_id, context)    
       
    elif query.data == "Departamentos":   
        await query.edit_message_text(text="Aquí tienes un mapa general de la universidad, Espero que te sea de ayuda.")
        chat_id = update.effective_chat.id
        await Mapa(chat_id, context)
    
    elif query.data == "Inscripcion":
        await query.edit_message_text(text="Aquí tienes la información sobre la inscripción.")
        chat_id = update.effective_chat.id
        await Inscripcion(chat_id, context)  
            
    elif query.data == "Actividades complementarias":
        await query.edit_message_text(text="Te muestro las actividades que puedes realizar")
        chat_id = update.effective_chat.id
        await actividades(chat_id, context) 
        
    #await query.edit_message_text(text=f"Selected option: {query.data}")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    # Malas Palabras
    groserias = [
    'estúpido','estupido','estupida','estúpida', 'imbécil', 'imbecil','idiota', 'pendejo','pendeja', 'maldito', 'cabrón', 'hijo de puta',
    'Puto', 'zorra', 'Puta', 'mierda', 'chingar', 'maricón','maricon', 'puto', 'culo','mamon', 'gordo', 'chingada', 'Chingada','cerdo', 'perra', 'pito', 
    'baboso', 'mamada','Tonto', 'naco', 'Tonta', 'jodido', 'desgraciado','tonto','tonta','inutil', 'pendejada','asqueroso','cojer', 
    'burrada','no sirves','mamar','pelar','chupar','chupas','pelas',]
    user_message = update.message.text.lower()

    Palabrota = [ "No digas groserias 😒", "Por favor, usa un lenguaje respetuoso ",
    "Evita usar palabras ofensivas 🤐","No permitimos este tipo de lenguaje",
    "Evitanos la pena de banearte del bot 🤭","No es necesario usar lenguaje ofensivo.","Nos reservamos el derecho de ayudarte 😵"]
    
    
    if any(word in user_message for word in groserias):
        palabrota= random.choice(Palabrota)
        await update.message.reply_text(palabrota)

    # falta desarrollar el baneo
    
   
   # despedida
    gracias=['Gracias','gracias'] 
   
    agradecimientos = [ 'Un gusto en ayudarte 😊', '¡De nada! Siempre aquí para ayudarte.',
    'No hay problema, ¡feliz de ayudar!', '¡Gracias a ti! 😊', '¡Con gusto!',
    '¡Siempre es un placer ayudar!', '¡A tu servicio!']

    if any(word in user_message for word in gracias):
        agradece = random.choice(agradecimientos)
        await update.message.reply_text(agradece)
   
   
   
   # Help
    if update.message.text == 'ayuda' or update.message.text == 'Ayuda':
        help_message = (
        "¡Hola! 😊 Aquí tienes la información que necesitas:\n\n"
        "Para abrir el menú de opciones, puedes:\n"
        "1. Escribir Menu o 😊.\n"
        "En el menú de opciones, encontrarás diversas funciones y servicios disponibles.\n\n"
        "Si necesitas más información o tienes alguna pregunta, no dudes en contactarnos al "
        "número 📞 7676718158.\n\n"
        "¡Estamos aquí para ayudarte!"
    )
        await update.message.reply_text(help_message)
  
        
    
    #Saludos
    saludos = ['Hola', 'hola', 'holi','Buenos días', 'buenos días', 'Buenas tardes', 'buenas tardes','Holi','AidMe']
    Respuestas = [ "¿Cómo puedo ayudarte hoy? 😁", "¡Hola! ¿En qué puedo asistirte? 😊","Holi ¿Qué necesitas? ","¡Hola! ¿Qué tal? 🤗"]

    if update.message.text in saludos:
        respuesta= random.choice(Respuestas)
        await update.message.reply_text(respuesta)
        
    # Menu     
    if update.message.text == '😊' or update.message.text == 'Menu'or update.message.text == 'menu' :  
       
        # Botones de  las opciones
        
        keyboard = [[InlineKeyboardButton('Credencial', callback_data='Credencial')], 
            [InlineKeyboardButton('Constancia', callback_data='Constancia')],
            [InlineKeyboardButton('Titulo', callback_data='Titulo')],
            [InlineKeyboardButton('Departamentos', callback_data='Departamentos'),
           ], [InlineKeyboardButton('Seguro social', callback_data='Seguro social'),
           ], [InlineKeyboardButton('Inscripcion', callback_data='Inscripcion'),
           ],[InlineKeyboardButton('Actividades complementarias', callback_data='Actividades complementarias'),
           ]]
        
        menu_choices = InlineKeyboardMarkup(keyboard)
        
        
# Send the message with menu
        await context.bot.send_message(
    chat_id=update.message.chat_id, text="Selección de servicios", reply_markup=menu_choices)
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
