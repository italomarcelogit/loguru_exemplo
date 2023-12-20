!pip install -q loguru
from loguru import logger
from datetime import datetime

logger.add("meuapp.log", format="{extra[ip]} | {extra[agora]} ({extra[user]}): {message}",
           rotation="1 week", backtrace=True, diagnose=True) 

logger.bind(user="mariajose").info("XPto:> usuário fez login com sucesso")

task_id=1
with logger.contextualize(task=task_id):
    calculo = 1 + 2
    logger.bind(user="mariajose").info(f"fim da tarefa {task_id}")

logger.bind(user="api_bancoXP").warning("Acesso não autorizado")
