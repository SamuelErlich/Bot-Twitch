# 🤖 Browser Bot Controller

Um bot em Python que automatiza a abertura de múltiplas instâncias do navegador com proxies diferentes, incluindo uma interface web moderna para controle e monitoramento.

## ✨ Funcionalidades

- **Múltiplas Instâncias**: Execute até 10 instâncias simultâneas do navegador
- **Suporte a Proxies**: HTTP, HTTPS e SOCKS5 com e sem autenticação
- **User-Agent Aleatório**: Rotação automática de user-agents para cada instância
- **Interface Web**: Controle completo através de uma interface web moderna
- **Upload de Proxies**: Carregue listas de proxies via arquivo .txt
- **Monitoramento**: Acompanhe o status e logs de execução em tempo real
- **Interações Simuladas**: Scroll automático e cliques em elementos da página

## 🚀 Deploy Rápido

### Railway (Recomendado)

1. Faça fork deste repositório
2. Conecte sua conta do Railway ao GitHub
3. Importe o projeto no Railway
4. O deploy será automático!

### GitHub Pages + Backend Separado

1. Faça fork deste repositório
2. Configure o backend no Railway ou Heroku
3. Atualize a URL da API no frontend

## 🛠️ Instalação Local

### Pré-requisitos

- Python 3.11+
- Chrome/Chromium instalado
- ChromeDriver compatível

### Passos

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/browser-bot-controller.git
cd browser-bot-controller
```

2. **Crie e ative o ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute a aplicação**
```bash
python src/main.py
```

5. **Acesse a interface**
Abra http://localhost:5000 no seu navegador

## 📝 Como Usar

### 1. Preparar Lista de Proxies

Crie um arquivo `proxies.txt` com um proxy por linha:

```
http://usuario:senha@192.168.1.1:8080
socks5://10.0.0.1:9050
http://172.16.0.1:3128
```

### 2. Configurar o Bot

1. Acesse a interface web
2. Defina a URL de destino
3. Configure o número de instâncias (1-10)
4. Faça upload do arquivo de proxies

### 3. Executar

1. Clique em "Iniciar Bot"
2. Monitore o status na interface
3. Use "Parar Bot" quando necessário

## 🔧 Configuração Avançada

### Formatos de Proxy Suportados

- **HTTP**: `http://host:porta` ou `http://user:pass@host:porta`
- **HTTPS**: `https://host:porta` ou `https://user:pass@host:porta`
- **SOCKS5**: `socks5://host:porta` ou `socks5://user:pass@host:porta`

### User-Agents Incluídos

O bot rotaciona automaticamente entre os seguintes user-agents:
- Chrome Windows/Mac
- Edge Windows
- Firefox Windows
- Safari Mac

### Interações Simuladas

Para cada instância, o bot executa:
1. Acesso à URL especificada
2. Scroll até o final da página
3. Tentativa de clique em links/botões visíveis
4. Aguardo de 2 segundos entre ações

## 📁 Estrutura do Projeto

```
browser-bot-controller/
├── src/
│   ├── main.py              # Aplicação Flask principal
│   ├── bot.py               # Lógica do bot de automação
│   ├── routes/
│   │   ├── bot.py           # Rotas da API do bot
│   │   └── user.py          # Rotas de usuário (template)
│   ├── models/
│   │   └── user.py          # Modelos de dados
│   ├── static/
│   │   └── index.html       # Interface web
│   └── database/
│       └── app.db           # Banco SQLite
├── venv/                    # Ambiente virtual
├── requirements.txt         # Dependências Python
├── Dockerfile              # Configuração Docker
├── .gitignore              # Arquivos ignorados pelo Git
└── README.md               # Este arquivo
```

## 🌐 API Endpoints

### Bot Control

- `GET /api/bot/status` - Status do bot
- `POST /api/bot/start` - Iniciar bot
- `POST /api/bot/stop` - Parar bot
- `POST /api/bot/upload-proxies` - Upload de proxies
- `GET /api/bot/proxies` - Listar proxies

### Exemplo de Uso da API

```javascript
// Iniciar bot
fetch('/api/bot/start', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        url: 'https://exemplo.com',
        num_instances: 3,
        proxy_file: 'proxies.txt'
    })
});
```

## 🔒 Considerações de Segurança

- Use proxies confiáveis
- Respeite os termos de serviço dos sites
- Configure rate limiting adequado
- Monitore o uso de recursos

## 🐛 Solução de Problemas

### ChromeDriver não encontrado
```bash
# Ubuntu/Debian
sudo apt-get install chromium-chromedriver

# Ou baixe manualmente
wget https://chromedriver.chromium.org/downloads
```

### Erro de permissão
```bash
chmod +x /usr/bin/chromedriver
```

### Proxy não funciona
- Verifique o formato do proxy
- Teste a conectividade manualmente
- Confirme credenciais de autenticação

## 📊 Monitoramento

A interface web fornece:
- Status em tempo real do bot
- Contagem de proxies carregados
- Logs de execução
- Controles de start/stop

## 🤝 Contribuição

1. Faça fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

## ⚠️ Aviso Legal

Este software é fornecido apenas para fins educacionais e de teste. O uso responsável é de responsabilidade do usuário. Sempre respeite os termos de serviço dos sites e as leis locais.

## 🆘 Suporte

Para suporte e dúvidas:
- Abra uma issue no GitHub
- Consulte a documentação
- Verifique os logs de erro

---

**Desenvolvido com ❤️ para automação web responsável**

# Bot-Twitch
