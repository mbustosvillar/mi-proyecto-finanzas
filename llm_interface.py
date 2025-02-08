import ollama

def ask_llm(prompt):
    response = ollama.chat(
        model="deepseek-r1",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']

if __name__ == "__main__":
    test = ask_llm("Explica la relación entre Sharpe Ratio y la optimización de portafolio")
    print(test)
