from flask import Blueprint, request, jsonify
import threading
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from src.bot import main as run_bot, load_proxies_from_file

bot_bp = Blueprint('bot', __name__)

# Variável global para controlar o estado do bot
bot_running = False
bot_thread = None

@bot_bp.route('/start', methods=['POST'])
def start_bot():
    global bot_running, bot_thread
    
    if bot_running:
        return jsonify({'error': 'Bot já está rodando'}), 400
    
    data = request.get_json()
    url = data.get('url', 'https://www.google.com')
    num_instances = data.get('num_instances', 2)
    proxy_file = data.get('proxy_file', 'proxies.txt')
    
    # Verificar se o arquivo de proxies existe
    proxy_path = os.path.join(os.path.dirname(__file__), proxy_file)
    if not os.path.exists(proxy_path):
        return jsonify({'error': f'Arquivo de proxies {proxy_file} não encontrado'}), 400
    
    def run_bot_thread():
        global bot_running
        try:
            bot_running = True
            run_bot(url, num_instances, proxy_path)
        finally:
            bot_running = False
    
    bot_thread = threading.Thread(target=run_bot_thread)
    bot_thread.start()
    
    return jsonify({
        'message': 'Bot iniciado com sucesso',
        'url': url,
        'num_instances': num_instances,
        'proxy_file': proxy_file
    })

@bot_bp.route('/stop', methods=['POST'])
def stop_bot():
    global bot_running, bot_thread
    
    if not bot_running:
        return jsonify({'error': 'Bot não está rodando'}), 400
    
    # Nota: Para uma implementação mais robusta, seria necessário
    # modificar o bot.py para aceitar sinais de parada
    bot_running = False
    
    return jsonify({'message': 'Comando de parada enviado'})

@bot_bp.route('/status', methods=['GET'])
def bot_status():
    global bot_running
    return jsonify({'running': bot_running})

@bot_bp.route('/upload-proxies', methods=['POST'])
def upload_proxies():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nenhum arquivo selecionado'}), 400
    
    if file:
        # Salvar o arquivo na pasta src
        filename = 'proxies.txt'
        filepath = os.path.join(os.path.dirname(__file__), filename)
        file.save(filepath)
        
        # Verificar quantos proxies foram carregados
        proxies = load_proxies_from_file(filepath)
        
        return jsonify({
            'message': 'Arquivo de proxies carregado com sucesso',
            'proxies_count': len(proxies)
        })

@bot_bp.route('/proxies', methods=['GET'])
def get_proxies():
    proxy_path = os.path.join(os.path.dirname(__file__), 'proxies.txt')
    if not os.path.exists(proxy_path):
        return jsonify({'proxies': []})
    
    proxies = load_proxies_from_file(proxy_path)
    return jsonify({'proxies': proxies})

