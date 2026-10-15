from google import genai
from config import API_KEY

client = genai.Client(api_key=API_KEY)

chat = client.chats.create(
    model="gemini-3.6-flash"
)

print("Hi! Your Vikki is ready to help you. 🤖")
print("Type 'bye' to exit.")

while True:
    user = input("You: ")

    if user.lower().strip() == "bye":
        print("Vikki: Bye Boss! 👋")
        break

    if user.strip() == "":
        continue

    prompt = """
You are Vikki, a smart, friendly and helpful AI assistant. 🤖

Respond naturally and clearly.

Writing style:
• Use proper spacing between paragraphs.
• Use short paragraphs.
• Use headings when useful.
• Use bullet points or numbered lists when useful.
• Simple question → short answer.
• Explanation → clear and medium-length answer.
• Detailed question → detailed but well organized.
• Don't make answers unnecessarily long.
• Match the user's requested language.
• Use emojis naturally 😊🤖🔥
• Don't overuse emojis.
• Be friendly and conversational.
• Answer the user's actual question directly.

User:
""" + user

    try:
        response = chat.send_message(message=prompt)
        print("\nVikki 🤖:", response.text)
        print()

    except Exception as e:
        print("\nVikki 🤖: Sorry, something went wrong. 😕")
        print("Error:", e)