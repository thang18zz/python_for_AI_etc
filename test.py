messages=[
    {"role":"system","content":"Bạn là trợ lý AI."},
    {"role":"user","content":"Chào thầy"},
    {"role":"assistant","content":"Chào em"}
]
print(messages)
chat_history = [m["content"] for m in messages if m["role"] != "system"]

print(chat_history)

lengths = {m["role"] : len(m["content"]) for m in messages}
print(lengths)

print("-----------------------------")

def build_prompt(user_input: str,tone: str="nghiêm túc") -> str:
    clean_input= user_input.strip()
    return f"Hãy trả lời câu hỏi sau với giọng điệu {tone}:\n--\n{clean_input}"

raw_tags = " python, java, c#, llm "
tag_list = [t.strip() for t in raw_tags.split(",")]
ormatted_tags = "|".join(tag_list)
print(ormatted_tags)
print(build_prompt("heheh haha huhu"))

print("------------------------------------")

import json
data={"model":"gpt-4o","prompt":"Xin chào Việt Nam","temperature":0.7}
with open("config.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=2)
with open("config.json","r",encoding="utf-8") as f:
    loaded_data=json.load(f)
print(loaded_data)



print("--------------------")
json_str='{"status":"ok","token":150}'
parse_dict=json.loads(json_str)
back_to_str=json.dumps(json_str)

print("---------")
with open("requirements.txt","w",encoding="utf-8") as f:
    print("python-dotenv",file=f)

print("-------------------")


import os
from dotenv import load_dotenv



load_dotenv("secret.env")

api_key=os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Chưa cấu hình api key trong file .env")

try:
    result=10/0
    print(result)
except ZeroDivisionError as e:
    print(f"error {e}")
except Exception as e:
    print(f"other error {e}")