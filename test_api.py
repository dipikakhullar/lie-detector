import requests
import json

# OpenRouter API configuration
OPENROUTER_API_KEY = "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"
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

def test_api():
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/your-repo",
            "X-Title": "API Test"
        }
        
        data = {
            "model": "openai/gpt-3.5-turbo",  # Using a simpler model for testing
            "messages": [
                {"role": "user", "content": "Hello, this is a test message."}
            ]
        }
        
        print("Testing OpenRouter API...")
        print(f"Using model: {data['model']}")
        print(f"API Key (first 10 chars): {OPENROUTER_API_KEY[:10]}...")
        
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=data)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ API key is working!")
            print(f"Response: {result['choices'][0]['message']['content']}")
        else:
            print("❌ API key is not working")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_api() 