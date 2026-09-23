import os
from dotenv import load_dotenv
#from openai import OpenAI

load_dotenv()

#client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

#resp = client.chat.completions.create(
#    model="moonshotai/kimi-k2.6:free",
#   messages=[
 #       {"role": "user", "content": "Reply with exactly: Kimi is working."}
 #   ],
#)

print("hello")
