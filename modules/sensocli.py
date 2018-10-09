from app.mac import mac, signals

@signals.message_received.connect
def handle(message):
     print(message.text)
     print(message)
