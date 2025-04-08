#STILL WORKING ON IT 

# 🗣️ Behalf 

## FLOW : (SEE AT END OF MD)

## 🔥 The Problem This AI Negotiation Agent Solves
❌ Existing Translation Apps Are Not Enough

Most translation apps (Google Translate, DeepL, etc.) simply convert words from one language to another—but they don’t handle real-life negotiations, deal-making, or complex conversations.

    🗣 No Context Awareness → Basic translators don’t remember past messages or understand context.
    🔄 No Conversation Flow → They translate sentence by sentence without engaging in a natural discussion.
    🤝 No Negotiation Skills → They don’t understand persuasion, bargaining, or deal-making like a human would.

### ✅ What This AI Agent Does Differently

This AI-powered negotiation assistant is more than just a translator—it’s a full conversational AI that can act on behalf of the user in a foreign language.
## 🎯 What Problems Does It Solve?

    ### 💬 Full-Conversation Handling
        Engages in complete discussions instead of just translating individual sentences.
        Maintains context and remembers past messages.

    ### 🤝 AI-Powered Negotiations
        Understands persuasion tactics and strategic bargaining.
        Can haggle prices, make counteroffers, and suggest better deals.
        Knows how to balance firmness and flexibility in a negotiation.

    ### 🧠 Adaptive and Goal-Oriented
        Understands user’s intent (e.g., getting the best price, closing a deal, solving a problem).
        Adapts its tone, politeness, and assertiveness based on the situation.
        Can mimic human negotiation styles (aggressive, diplomatic, cooperative).

    ### 🌍 Multilingual Real-Time Conversations
        Works in multiple languages dynamically.
        Can talk on behalf of the user in a language they don’t know.
        Uses ElevenLabs for natural, human-like speech synthesis.

    ### 🎭 Emotion & Cultural Awareness
        Detects emotion and intent in conversations.
        Adjusts responses based on cultural norms and politeness levels.

## 🔥 Real-World Use Cases

    🛒 Business Deals & Negotiations → Helps users haggle prices, close deals, and get better offers in another language.
    ✈️ International Travel Assistance → Can speak to locals, book reservations, or handle disputes on behalf of a traveler.
    🎙 Live Interpretation & Mediation → Acts as a real-time interpreter while negotiating contracts, agreements, or partnerships.
    🛠 Customer Support & Dispute Resolution → Can talk to customer service reps in their language to resolve issues.




## 🌍 Overview  
This project is an **AI-powered negotiation assistant** that can:  
✅ Listen to a user’s audio in one language  
✅ Translate and generate responses in another language  
✅ Speak on behalf of the user using **ElevenLabs TTS**  
✅ Engage in negotiations using **CrewAI** and **LLMs**  
✅ Communicate in real-time via **Flask WebSockets**  

---

## 🚀 Features  
- 🎤 **Real-time speech-to-text (STT)** using Whisper  
- 🧠 **AI response generation** using OpenAI’s GPT-4 or Claude or Deepseek R-1
- 🌎 **Translation engine** for multi-language support  
- 🗣️ **Text-to-Speech (TTS)** with ElevenLabs  
- 🔁 **Full-duplex WebSocket communication** for real-time interaction  
- 🏗 **Modular CrewAI framework** for intelligent decision-making  

---

🏗️ How It Works

1️⃣ User speaks → Audio is captured and sent to Flask WebSocket.
2️⃣ Whisper STT → Converts speech to text.
3️⃣ Ai Agent Decide What to Talk In What Tone And Genrate Response based on Goal and Current Happening Conversation
4️⃣ Translation → Converts text to another language.
5️⃣ LLM (GPT-4, Claude, etc.) → AI generates a response.
6️⃣ TTS (ElevenLabs) → Converts AI response to Realistic speech.
![image](https://github.com/user-attachments/assets/7093d8b4-3e05-49a6-92fe-7b6e6d497639)

![Editor _ Mermaid Chart-2025-04-08-002435](https://github.com/user-attachments/assets/f9392206-2b42-4450-bac3-fb5fb621e36e)
