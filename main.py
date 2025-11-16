from ollama import Client
client = Client(host="http://127.0.0.1:11434")
history_a = []
history_b = []
OUTPUT_FILE = "conversation.md"
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("# AI Conversation: Jake & Paul\n\n")
def write_md(name, text):
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write(f"## {name}\n\n{text}\n\n")
def chat(model, history, new_message):
    history.append({"role": "user", "content": new_message})
    response = client.chat(model=model, messages=history)
    assistant_msg = response["message"]["content"]
    history.append({"role": "assistant", "content": assistant_msg})
    return assistant_msg
msg = "Hello!"
while True: reply_a = chat("gemma3:1b", history_a, msg); print("Jake:", reply_a); write_md("Jake", reply_a); reply_b = chat("gemma3:1b", history_b, reply_a); print("Paul:", reply_b); write_md("Paul", reply_b); msg = reply_b