from google import generativeai as ai

apikey='your_api_key'
ai.configure(api_key=apikey)
model =ai.GenerativeModel("gemini-2.0-flash-exp-image-generation")
chat=model.start_chat()

while True:
    message=input("you: ")
    if message.lower()=='bye':
        print("Gemini: GoodBye")
        break
    response=chat.send_message(message)
    print("Gemini:",response.text)
    
