import os
from google import genai
from dotenv import load_dotenv
from google.genai import types
import time

load_dotenv()

# print(os.environ.get("GEMINI_API_KEY"))
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


question = input("Question: ")
system_prompt = "You are a beginner-friendly backend teacher."
temperature = 1

start_time = time.perf_counter()

res = client.models.generate_content(
    model="models/gemini-3-flash-preview",
    # contents="Explain Self attention in transformer"
    contents=question,
    config=types.GenerateContentConfig(
     system_instruction = system_prompt,
     temperature= temperature
    )
)

end_time = time.perf_counter()

latancy =  end_time - start_time

print("\n---------- RESPONSE ----------")
print(res.text)
print("\n---------- METRICS ----------")


usage = res.usage_metadata
if usage:
    print("Input tokens:", usage.prompt_token_count)
    print("Output tokens:", usage.candidates_token_count)
    print("Total tokens:", usage.total_token_count)

print(f"Latancy: {latancy:.2f} seconds")
