import json
import os
from typing import Any, Dict
from litellm import completion
from dotenv import load_dotenv

load_dotenv() 
api_key = os.getenv("GROQ_API_KEY")

MODEL = "groq/llama-3.3-70b-versatile"

def get_itinerary(destination: str) -> Dict[str, Any]:
    messages = [
        {
            "role": "system",
            "content": "You are a helpful travel assistant. Output valid JSON."
        },
        {
            "role": "user",
            "content": f"""
            Generate a travel itinerary for {destination}.
            Return a JSON object with strictly these keys: 
            "destination", "price_range", "ideal_visit_times", "top_attractions".
            """
        }
    ]

    response = completion(
        model=MODEL,
        messages=messages,
        api_key=api_key, 
        response_format={"type": "json_object"}
    )
    
    content = response.choices[0].message.content
    data = json.loads(content)
    
    return data