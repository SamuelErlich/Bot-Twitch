# 🚀 Guia de Deploy - Browser Bot Controller

## 📋 Pré-requisitos para Deploy

### Para GitHub
- Conta no GitHub
- Repositório criado

### Para Railway
- Conta no Railway (railway.app)
- Conta do GitHub conectada ao Railway

## 🔧 Preparação dos Arquivos

Antes de fazer o deploy, certifique-se de que você tem todos estes arquivos:

```
browser-bot-controller/
├── src/
│   ├── main.py
│   ├── bot.py
│   ├── routes/
│   ├── models/
│   ├── static/
│   └── database/
├── requirements.txt
├── Dockerfile
├── railway.json
├── .gitignore
├── README.md
└── DEPLOY.md
```

## 📤 Deploy no GitHub

### 1. Criar Repositório

```bash
# No seu computador local
git init
git add .
git commit -m "Initial commit: Browser Bot Controller"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/browser-bot-controller.git
git push -u origin main
```

### 2. Configurar Repositório

1. Acesse seu repositório no GitHub
2. Vá em **Settings** > **Pages**
3. Configure a fonte como "Deploy from a branch"
4. Selecione a branch `main` e pasta `/` (root)
5. Salve as configurações

**Nota**: O GitHub Pages só serve arquivos estáticos. Para o backend, use Railway.

## 🚂 Deploy no Railway

### Método 1: Deploy Direto (Recomendado)

1. **Acesse Railway**
   - Vá para https://railway.app
   - Faça login com sua conta GitHub

2. **Criar Novo Projeto**
   - Clique em "New Project"
   - Selecione "Deploy from GitHub repo"
   - Escolha seu repositório `browser-bot-controller`

3. **Configuração Automática**
   - Railway detectará automaticamente o `Dockerfile`
   - O build começará automaticamente
   - Aguarde a conclusão (5-10 minutos)

4. **Configurar Domínio**
   - Após o deploy, clique em "Settings"
   - Vá para "Networking"
   - Clique em "Generate Domain"
   - Sua aplicação estará disponível em: `https://seu-app.railway.app`

### Método 2: Railway CLI

```bash
# Instalar Railway CLI
npm install -g @railway/cli

# Login
railway login

# Inicializar projeto
railway init

# Deploy
railway up
```

## 🔧 Configurações Importantes

### Variáveis de Ambiente (Railway)

No painel do Railway, configure estas variáveis se necessário:

```
PORT=5000
FLASK_ENV=production
SECRET_KEY=sua_chave_secreta_aqui
```

### Recursos Recomendados

- **CPU**: 1 vCPU (mínimo)
- **RAM**: 1GB (mínimo, 2GB recomendado)
- **Storage**: 1GB

## 🧪 Testando o Deploy

### 1. Verificar Saúde da Aplicação

```bash
curl https://seu-app.railway.app/api/bot/status
```

Resposta esperada:
```json
{"running": false}
```

### 2. Testar Interface Web

1. Acesse `https://seu-app.railway.app`
2. Verifique se a interface carrega
3. Teste o upload de proxies
4. Teste iniciar/parar bot

### 3. Monitorar Logs

No Railway:
1. Vá para seu projeto
2. Clique na aba "Deployments"
3. Clique no deployment ativo
4. Veja os logs em tempo real

## 🐛 Solução de Problemas

### Build Falha

**Erro**: `ChromeDriver not found`
```dockerfile
# Adicione no Dockerfile
RUN apt-get update && apt-get install -y chromium-driver
```

**Erro**: `Permission denied`
```dockerfile
# Adicione no Dockerfile
RUN chmod +x /usr/bin/chromedriver
```

### Deploy Falha

**Erro**: `Port already in use`
```python
# Em src/main.py, use a porta do Railway
import os
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
```

**Erro**: `Module not found`
```bash
# Verifique requirements.txt
pip freeze > requirements.txt
```

### Runtime Errors

**Erro**: `Chrome crashed`
```python
# Adicione mais opções no bot.py
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
```

## 📊 Monitoramento

### Logs Importantes

```bash
# Railway CLI
railway logs

# Ou no painel web
# Deployments > [deployment] > Logs
```

### Métricas

No Railway, monitore:
- CPU usage
- Memory usage
- Network traffic
- Response times

## 🔄 Atualizações

### Deploy Automático

1. Faça push para o GitHub
2. Railway detectará automaticamente
3. Novo deploy será iniciado
4. Zero downtime deployment

### Deploy Manual

```bash
# Railway CLI
railway up --detach
```

## 🔐 Segurança

### Recomendações

1. **Não commite proxies**: Adicione `proxies.txt` no `.gitignore`
2. **Use HTTPS**: Railway fornece SSL automático
3. **Rate Limiting**: Implemente rate limiting se necessário
4. **Monitoramento**: Configure alertas para uso excessivo

### Variáveis Sensíveis

```bash
# Railway CLI
railway variables set SECRET_KEY=sua_chave_aqui
railway variables set PROXY_PASSWORD=senha_proxy
```

## 📞 Suporte

### Railway
- Documentação: https://docs.railway.app
- Discord: https://discord.gg/railway
- Status: https://status.railway.app

### GitHub
- Documentação: https://docs.github.com
- Support: https://support.github.com

## ✅ Checklist Final

Antes de considerar o deploy completo:

- [ ] Repositório GitHub criado e configurado
- [ ] Deploy no Railway funcionando
- [ ] Interface web acessível
- [ ] API endpoints respondendo
- [ ] Upload de proxies funcionando
- [ ] Bot iniciando/parando corretamente
- [ ] Logs sendo gerados
- [ ] Domínio personalizado configurado (opcional)
- [ ] Monitoramento ativo
- [ ] Documentação atualizada

---

**🎉 Parabéns! Seu Browser Bot Controller está online!**

Acesse: `https://seu-app.railway.app`

