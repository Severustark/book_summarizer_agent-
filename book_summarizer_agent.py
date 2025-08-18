# book_summarizer_agent.py

import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

load_dotenv()

llm = ChatOpenAI(temperature=0.5)

def basic_book_prompt(book_title: str) -> str:
    return f"""
    Sen kitaplara dair derinlemesine analiz yapabilen bir yapay zekasın.
    Kitabın adı: {book_title}

    1. Kitabın kısa özeti nedir?
    2. Ana temaları nelerdir?
    3. Hangi kitleye hitap eder?
    4. Bu kitaba benzeyen başka hangi kitapları önerirsin?

    Cevaplarını anlaşılır ve kısa paragraf şeklinde ver.
    """

def book_insight_tool(book_title: str) -> str:
    prompt = basic_book_prompt(book_title)
    return llm.predict(prompt)

# Aracı tanımlıyoruz
book_tool = Tool(
    name="BookInsight",
    func=book_insight_tool,
    description="Kitap adı verildiğinde özet ve tematik analiz yapar."
)

# Agent'i başlat
agent = initialize_agent(
    tools=[book_tool],
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

if __name__ == "__main__":
    book_title = input("Kitap adını girin: ")
    result = agent.run(f"{book_title} kitabını analiz et")
    print(result)
