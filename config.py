import os
import ProxyCloud

BOT_TOKEN = '5363620265:AAFZ0WJTfRrGHAtOMDGuyxoNQe1RqUfg3Oo' #Aqui va el token del bot
API_ID =  12168140 #Tu api id de telegram
API_HASH = '3504ce0eddb7dff4288d05d5e3dc5e4c' #Tu api id de telegram
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','quejestoniuyol').split(';')

static_proxy = '' #agrega si kieres tener un proxy statico Con @quejestoniuyol si kieres comprar un proxy
PROXY = ProxyCloud.parse(static_proxy)

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
  
#Lo siguiente son las tablas de la base de datos de usarios, 
#es obligatorio agregar a aquellos usarios estaticos puestos en el main.py
#los agregados mediante /add no es necesario
#ponerlos valor 0 siempre

space = {}
space['quejestoniuyol'] = 0
