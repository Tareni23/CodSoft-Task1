#Chatbot in python 
def chatbot(user_input):
    responses={
        "hi":"hello!"
        "how are you":"I'm fine, thank you",
        "what are you doing":"thinking about you",
        "bye":"goodbye",
        "default":"I didn't understand",
    }

    #coversion for case matching
    user_input=user_input.lower()

    if user_input in responses:
        return responses[user_input]
    else:
        return responses["default"]

    print(chatbot("hi"))
    print(chatbot("how are you"))
    print(chatbot("what is the time?"))
    print(chatbot("bye"))
