!pip install -q loguru
from loguru import logger
from datetime import datetime

logger.add("meuapp.log", format="{extra[ip]} | {extra[agora]} ({extra[user]}): {message}",
           rotation="1 week", backtrace=True, diagnose=True) 

agora = datetime.now().strftime("%Y-%d-%m %H:%M:%S")
logger.bind(ip="192.168.50.1", agora=agora, user="mariajose").info("XPto:> usuário fez login com sucesso")

task_id=1
with logger.contextualize(task=task_id):
    calculo = 1 + 2
    logger.bind(ip="192.168.50.1", agora=agora,user="mariajose").info(f"fim da tarefa {task_id}")

logger.bind(ip="192.168.50.1", agora=agora, user="api_bancoXP").warning("Acesso não autorizado")
