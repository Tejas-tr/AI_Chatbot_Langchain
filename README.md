# 🤖 LangChain Memory Chatbot

A simple command-line chatbot built with **LangChain** and **OpenAI**, capable of remembering the conversation history so it can answer context-aware follow-up questions (e.g. "what is my name?").

---

## ✨ Features

- 💬 **Conversational memory** — tracks the full chat history using `HumanMessage` / `AIMessage` objects so the model can recall earlier context.
- 🧠 **Prompt templating** — uses `ChatPromptTemplate` with a `MessagesPlaceholder` to inject history dynamically into every request.
- 🔗 **LangChain pipeline** — clean `prompt | model | parser` chain for readable, composable logic.
- 🖥️ **Interactive CLI loop** — chat live in the terminal, type `quit` or `exit` to end the session.
- ⚙️ **Configurable model** — swap between models like `gpt-4o-mini` or `gpt-5-nano` with a one-line change.

---

## 🗂️ Project Structure

```
.
├── chat_lc.py        # Minimal demo: single-turn call with pre-seeded history
├── chatbot_lc_.py     # Full interactive chatbot loop with live memory
└── .env               # Stores your OPENAI_API_KEY (not committed)
```

---

## 🛠️ Tech Stack

| Component        | Purpose                                  |
|-------------------|-------------------------------------------|
| `langchain-openai`| Connects LangChain to OpenAI's chat models |
| `langchain-core`  | Prompt templates, message types, parsers  |
| `python-dotenv`   | Loads API keys from a `.env` file         |

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/langchain-memory-chatbot.git
cd langchain-memory-chatbot
```

### 2. Install dependencies
```bash
pip install langchain langchain-openai langchain-core python-dotenv
```

### 3. Set up your API key
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Run the chatbot
```bash
python chatbot_lc_.py
```

Example session:
```
Chat with bot, type quit or exit to stop conversation
you : My name is Alex
Hi Alex! How can I help you today?
 history row has 2 messages
you : what is my name?
Your name is Alex.
 history row has 4 messages
you : exit
```

---

## 🧩 How It Works

1. A `ChatPromptTemplate` defines the conversation structure: a system message, a placeholder for chat history, and the current human question.
2. Each turn, the growing `history` list (of `HumanMessage` / `AIMessage` objects) is passed into the chain along with the new question.
3. The chain (`prompt | model | parser`) sends everything to the OpenAI model and returns a clean string response.
4. The new question and response are appended to `history`, so the bot "remembers" the conversation for the next turn.

---

## 🔮 Roadmap

- [ ] Persist chat history to disk/database between sessions
- [ ] Add streaming responses for real-time output
- [ ] Wrap in a Gradio/Streamlit UI for a shareable web demo
- [ ] Add support for system-prompt customization via CLI flags

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

Built with [LangChain](https://www.langchain.com/) and [OpenAI](https://openai.com/).
