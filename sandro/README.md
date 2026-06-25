# Oráculo IA

Jogo de adivinhação de personagens que combina **inferência bayesiana** (raciocínio probabilístico clássico) com um **LLM** (Llama 3.3 70B, via Groq).

O LLM:
- reescreve cada pergunta de forma natural e variada;
- narra o palpite final de forma dramática;
- monta a "ficha" de atributos quando você ensina um personagem novo.

Se a internet ou o LLM falharem, o motor bayesiano continua jogando sozinho (degradação graciosa).

## Como rodar

1. Instale as dependências:

   ```
   pip install flask requests
   ```

2. Pegue uma chave gratuita em https://console.groq.com e defina no ambiente:

   - Linux / macOS:
     ```
     export GROQ_API_KEY="sua_chave_aqui"
     ```
   - Windows (PowerShell):
     ```
     $env:GROQ_API_KEY="sua_chave_aqui"
     ```

3. Suba o servidor:

   ```
   python app.py
   ```

4. Abra no navegador: http://localhost:5000

## Estrutura

- `app.py` — servidor Flask: entrega a página e faz a ponte com o Groq (sua chave fica no servidor, nunca no navegador).
- `index.html` — o jogo: motor bayesiano + camada LLM, com chave de liga/desliga do LLM para a apresentação.

## Dica para a apresentação

O botão **"usar LLM"** liga e desliga o LLM ao vivo. Desligado, dá pra mostrar a IA clássica (Bayes) sozinha; ligado, mostra o LLM enriquecendo a experiência. Bom para explicar a arquitetura híbrida.
