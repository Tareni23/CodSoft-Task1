def chatbot():
  while True:

        user_input=input("\n User: ")

        if user_input=="hi":

            print("dev:- hi!")
            print("how can I help you?")

        elif user_input=="what is your name":

            print("dev:- my name is Dev-the friendly chatbot")

        elif  user_input=="what is the date today":

            from datetime import date

            date=date.today()

            print("dev:- today's date is ",date)

        elif user_input=="bye":

            print("dev:- bye!,Goodnight")

            break

        else:

            print("dev:- sorry!...I didn't Understand")

chatbot()
