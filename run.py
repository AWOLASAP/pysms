# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request, redirect
from twilio import twiml
from twilio.twiml.messaging_response import Message, MessagingResponse
import os


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming():
    """Respond to the sms with the messege sent.."""
    # Get the sent messege
    messageIn = request.values.get('Body', None)
    print("In:\n", messageIn) 

    # Create a file with the wanted python code in it
    with open("python_code.py", "w") as f:
        f.write(messageIn)

    # Clear output file and save output of code to an output file
    os.system('>output.txt; echo "Your code: " >> output.txt; python python_code.py >> output.txt')

    # Start our response
    resp = MessagingResponse()

    # Get message for response
    with open("output.txt", "r") as f:
        messageOut = f.read()
        print ("Out:\n", messageOut)
        if len(messageOut) <= 12 :
           messageOut = "You have an error in your code." 
        else:
            print(len(messageOut))

    # Add a message
    resp.message('\n ' + messageOut)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
