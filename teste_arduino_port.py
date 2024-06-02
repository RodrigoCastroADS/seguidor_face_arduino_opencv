from pyfirmata import Arduino, util
import time

port = 'COM3'  # Substitua pela porta correta
try:
    board = Arduino(port)
    print(f"Conectado ao Arduino na porta {port}")
    board.exit()
except Exception as e:
    print(f"Erro ao conectar com a porta {port}: {e}")
