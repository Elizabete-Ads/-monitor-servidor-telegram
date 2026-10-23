import requests

TOKEN = "8945606201:AAFD5QX1y8gX8NYzWI-QqlPmjdGF_v7d2L4"
CHAT_ID = "5233477871"
SERVIDOR_ALVO = "https://um-servidor-que-nao-existe-mesmo.com"

# URL estruturada corretamente para a API do Telegram
url_api = f"https://telegram.org{TOKEN}/sendMessage"

print(f"🤖 Robô Iniciado! Testando o servidor: {SERVIDOR_ALVO}")

try:
    # O robô testa o servidor alvo
    checagem = requests.get(SERVIDOR_ALVO, timeout=5)
    
    if checagem.status_code == 200:
        print("✅ Servidor ONLINE. Nenhuma ação necessária.")
    else:
        mensagem = f"⚠️ ALERTA: O servidor {SERVIDOR_ALVO} retornou erro {checagem.status_code}!"
        requests.post(url_api, data={"chat_id": CHAT_ID, "text": mensagem})
        print("🚨 Alerta enviado ao Telegram.")

except requests.exceptions.RequestException:
    # Cai aqui caso o servidor esteja totalmente offline
    mensagem = f"🚨 URGENTE: O Servidor {SERVIDOR_ALVO} está totalmente OFFLINE!"
    print("Enviando alerta para a URL correta do Telegram...")
    resposta = requests.post(url_api, data={"chat_id": CHAT_ID, "text": mensagem})
    
    if resposta.status_code == 200:
        print("✨ SUCESSO! Alerta enviado com sucesso ao seu celular!")
    else:
        print(f"❌ Falha no envio do alerta. Código: {resposta.status_code}")
