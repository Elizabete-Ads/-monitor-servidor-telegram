# 🤖 Monitor de Servidores Automatizado com Alertas via Telegram

Projeto desenvolvido focado em **Automação de Infraestrutura (DevOps/SRE/NOC)**. O script monitora a disponibilidade de servidores web e envia notificações resilientes em tempo real para a equipe técnica através da API de bots do Telegram.

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Linguagem:** Python 3
* **Ambiente:** Linux (Ubuntu)
* **Gerenciamento de Dependências:** Ambiente Virtual Python (`venv`)
* **Principais Bibliotecas:** `requests` para chamadas HTTP e `urllib3` para tratamento de sessões.

## 🧠 Desafios Solucionados & Aprendizados Técnicos
Durante o desenvolvimento do script, foram aplicadas boas práticas de engenharia de confiabilidade:
1. **Tratamento de Exceções Avançado:** Implementação de tratamento robusto para erros de DNS (`NameResolutionError`), quedas abruptas de conexão e timeouts de rede.
2. **Resolução de Bugs de Rede:** Correção de falhas críticas de parse de localização (`LocationParseError`), ajustando o endereçamento de hosts de API do Telegram de acordo com as especificações oficiais.
3. **Gerenciamento de Ambientes Linux:** Resolução de travas de memória e eliminação de processos fantasma em segundo plano usando ferramentas de terminal.

## 🚀 Como Executar o Projeto
1. Clone este repositório.
2. Ative o seu ambiente virtual: `source venv/bin/activate`
3. Instale as dependências: `pip install requests`
4. Execute o monitor: `python3 monitor.py`
