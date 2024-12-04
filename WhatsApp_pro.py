import pywhatkit as kit
import time

def send_auto_reply(phone_number, message):
 
    try:
        # Schedule the message to be sent 1 minute from now (pywhatkit handles timing)
        kit.sendwhatmsg(phone_number, message, time.localtime().tm_hour, time.localtime().tm_min + 1)
        print(f"Message scheduled to {phone_number}.")
    except Exception as e:
        print(f"An error occurred: {e}")



phone_number = "+918409840049" 
message = "Thank you for your message! We will get back to you soon."
send_auto_reply(phone_number, message)
