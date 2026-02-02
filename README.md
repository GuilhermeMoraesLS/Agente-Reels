# 🎬 Agente de Conteúdo - AI Content Creator Assistant

Um agente de IA inteligente que analisa vídeos de criadores de conteúdo e gera copywriting baseado em suas transcrições. Construído com AgentOS, OpenAI GPT-4, Groq Whisper e uma interface moderna em Next.js.

![Agent UI](https://img.shields.io/badge/Agent-UI-blue)
![Python](https://img.shields.io/badge/Python-3.13+-green)
![Next.js](https://img.shields.io/badge/Next.js-15-black)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Funcionalidades

- 🎥 **Transcrição Automática**: Converte vídeos em texto usando Groq Whisper
- 🤖 **Agente Inteligente**: Analisa transcrições e gera conteúdo personalizado
- 💬 **Interface Moderna**: Chat UI interativa construída com Next.js e shadcn/ui
- 🔍 **Busca Web**: Integração com Tavily para pesquisas contextuais
- 💾 **Memória Persistente**: Armazena contexto e histórico de conversas
- 🎨 **Multi-criador**: Suporta múltiplos criadores de conteúdo

## 📋 Pré-requisitos

Antes de começar, você precisará ter instalado:

- [Python 3.13+](https://www.python.org/downloads/)
- [Node.js 18+](https://nodejs.org/)
- [pnpm](https://pnpm.io/installation) (gerenciador de pacotes)
- [FFmpeg](https://ffmpeg.org/download.html)

### Instalando FFmpeg

**Windows:**
1. Baixe o FFmpeg em [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Extraia para `C:\ffmpeg`
3. Adicione `C:\ffmpeg\bin` ao PATH do sistema

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/agente-conteudo.git
cd agente-conteudo
```

### 2. Configure o Backend (Python)

```bash
# Crie um ambiente virtual
python -m venv .venv

# Ative o ambiente virtual
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Instale as dependências
pip install -e .
```

### 3. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# OpenAI API Key (obrigatório)
OPENAI_API_KEY=sua-chave-aqui

# Groq API Key (obrigatório para transcrição)
GROQ_API_KEY=sua-chave-aqui

# Tavily API Key (obrigatório para busca web)
TAVILY_API_KEY=sua-chave-aqui

# Caminho do FFmpeg (Windows)
FFMPEG_BIN=C:\ffmpeg\bin\ffmpeg.exe
# macOS/Linux (geralmente não é necessário se estiver no PATH)
# FFMPEG_BIN=/usr/local/bin/ffmpeg
```

#### 🔑 Como obter as API Keys:

- **OpenAI**: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- **Groq**: [https://console.groq.com/keys](https://console.groq.com/keys)
- **Tavily**: [https://tavily.com](https://tavily.com)

### 4. Configure o Frontend (Next.js)

```bash
cd agent-ui
pnpm install
```

## 📁 Organizando seus Vídeos

Coloque seus vídeos na pasta `videos/` seguindo esta estrutura:

```
videos/
├── criador1/
│   ├── video1.mp4
│   ├── video2.mp4
│   └── video3.mp4
└── criador2/
    ├── video1.mp4
    └── video2.mp4
```

**Exemplo:**

```
videos/
├── alexhormozi/
│   ├── marketing-tips.mp4
│   └── sales-strategy.mp4
└── garyvee/
    ├── social-media.mp4
    └── entrepreneurship.mp4
```

## 🎯 Uso

### Passo 1: Transcrever os Vídeos

Na raiz do projeto (com o ambiente virtual ativado):

```bash
python transcripter.py
```

Isso irá:
- Extrair o áudio de cada vídeo
- Transcrever usando Groq Whisper
- Salvar em `transcripts.json`

### Passo 2: Iniciar o Backend

```bash
python agent.py
```

O servidor estará rodando em `http://localhost:7777`

### Passo 3: Iniciar o Frontend

Em um novo terminal:

```bash
cd agent-ui
pnpm dev
```

Acesse `http://localhost:3000` no navegador

## 💡 Como Usar o Agente

1. **Liste os criadores disponíveis:**
   ```
   Quais criadores estão disponíveis?
   ```

2. **Peça análises específicas:**
   ```
   Analise o conteúdo do Alex Hormozi e crie um post para LinkedIn
   ```

3. **Gere conteúdo personalizado:**
   ```
   Crie um script de vídeo curto baseado nas transcrições do Gary Vee
   ```

## 🛠️ Tecnologias Utilizadas

**Backend:**
- [Agno](https://github.com/agno-agi/agno) - Framework para agentes de IA
- [OpenAI GPT-4](https://openai.com) - Modelo de linguagem
- [Groq Whisper](https://groq.com) - Transcrição de áudio
- [Tavily](https://tavily.com) - Busca web
- [FastAPI](https://fastapi.tiangolo.com) - API REST
- [SQLite](https://www.sqlite.org) - Banco de dados

**Frontend:**
- [Next.js 15](https://nextjs.org) - Framework React
- [TypeScript](https://www.typescriptlang.org) - Tipagem estática
- [Tailwind CSS](https://tailwindcss.com) - Estilização
- [shadcn/ui](https://ui.shadcn.com) - Componentes UI
- [Framer Motion](https://www.framer.com/motion) - Animações

## 📂 Estrutura do Projeto

```
agente-conteudo/
├── agent.py                 # Configuração do agente
├── transcripter.py          # Script de transcrição
├── transcription_reader.py  # Leitor de transcrições
├── transcripts.json         # Transcrições salvas
├── .env                     # Variáveis de ambiente
├── prompts/
│   └── copywriter.md       # Prompt do agente
├── videos/                 # Seus vídeos (você adiciona)
│   ├── criador1/
│   └── criador2/
├── tmp/
│   └── storage.db          # Banco de dados do agente
└── agent-ui/               # Interface web
    ├── src/
    └── package.json
```

## 🔧 Personalização

### Modificar o Prompt do Agente

Edite o arquivo [`prompts/copywriter.md`](prompts/copywriter.md) para personalizar o comportamento do agente.

### Adicionar Novas Ferramentas

Em [`agent.py`](agent.py), adicione novas ferramentas ao array `tools`:

```python
tools=[
    TavilyTools(), 
    list_available_creators, 
    get_creator_transcriptions,
    # Suas ferramentas personalizadas aqui
]
```

## 🐛 Troubleshooting

**Erro: "cannot import name 'get_transcriptions_for_creator'"**
- Certifique-se de que [`agent.py`](agent.py) está importando `get_creator_transcriptions` corretamente

**Erro: "FFmpeg not found"**
- Verifique se o FFmpeg está instalado e no PATH
- No Windows, configure `FFMPEG_BIN` no `.env`

**Erro: "No creators found"**
- Execute `python transcripter.py` primeiro
- Verifique se os vídeos estão na pasta `videos/`

**Frontend não conecta ao backend:**
- Certifique-se de que o backend está rodando em `http://localhost:7777`
- Verifique as configurações de endpoint na UI

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um Fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 👤 Autor

Guilherme de Moraes Lopes Silva
- LinkedIn: [Meu Perfil](https://www.linkedin.com/in/guilherme-de-moraes-82b6152b6/)

