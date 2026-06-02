from fastapi import APIRouter

from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
)

from app.services.chat_service import (
    ChatService,
)

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
)

service = ChatService()


@router.post(
    "",
    response_model=ChatResponse,
)
async def chat(
    request: ChatRequest,
):

    result = service.ask(
        request.question
    )

    return ChatResponse(
        answer=result["answer"],
        sources=result["sources"],
    )
