import os
from ollama import Client
client = Client(host="http://127.0.0.1:11434")
history_a = []
history_b = []
os.makedirs("conversations", exist_ok=True)
def get_next_filename():
    i = 1
    while True:
        path = f"conversations/conversation{i}.md"
        if not os.path.exists(path):
            return path
        i += 1
OUTPUT_FILE = get_next_filename()
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
global msg
CHAT_MODEL = "gemma3:1b"
msg = input("Starter message: \n")
SYSPROMT_A = input("Jake's system prompt:\n")
SYSPROMT_B = input("Paul's system prompt:\n")
history_a.append({"role": "system", "content": SYSPROMT_A})
history_b.append({"role": "system", "content": SYSPROMT_B})
def mainloop():
    global msg
    for i in range(250):
        reply_a = chat(CHAT_MODEL, history_a, msg)
        print("Jake:", reply_a)
        write_md("Jake", reply_a)

        reply_b = chat(CHAT_MODEL, history_b, reply_a)
        print("Paul:", reply_b)
        write_md("Paul", reply_b)

        msg = reply_b
while True:
    mainloop()
    match input("Do you want to continue? (y/n):\n"):
        case "y":
            print("Continueing")
        case "n":
            break
