from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

from . import conversation

bot = ChatBot(
    "chatbot",
    read_only=False,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "Sorry, I can't understand!",
            "maximum_similarity_threshold": 0.90,
        }
    ],
)


# chatterBotCorpusTrainer = ChatterBotCorpusTrainer(bot)
# chatterBotCorpusTrainer.train('chatterbot.corpus.english')

list_trainer = ListTrainer(bot)
list_trainer.train(conversation.list_to_train)


# Create your views here.


def index(request):
    return render(request, "bot/index.html")


def specific(request):
    return HttpResponse("Specific")


# def article(request, article_id):
#     # return HttpResponse(article_id)
#     return render(request, "bot/index.html", {"article_id": article_id})


def getResponse(request):
    userMessage = request.GET.get("userMessage")
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)
