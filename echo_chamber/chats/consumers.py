from channels.generic.websocket import JsonWebsocketConsumer


# Consumers are akin to views, this one is intended to show user's online status and send notifications
class ChatConsumer(JsonWebsocketConsumer):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_name = None

    def connect(self):
        print("Connected!")
        self.room_name = "home"
        self.accept()
        self.send_json(
          {
              "type": "Welcom_message",
              "message": "Hey there! You've successfully connected!",
          }
        )

    def disconnect(self, code):
        print("Disconnnected!")
        return super().disconnect(code)  

    def receive_json(self, content, **kwargs):
        print(content)
        return super().receive_json(content, **kwargs)