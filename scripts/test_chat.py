from app.services.chat_service import (
    ChatService,
)

service = ChatService()

response = service.ask(
    "What is asked to do in this assignment?"
)

print(response["answer"])
print(response["sources"])
