from django.shortcuts import render
from django.http import JsonResponse
import openai

# Create your views here.
openai.api_key = "sk-mc*****8hp4ijHBmpoBT************************"


def Sentiment_analysis(text):
    messages = [
        {
            "role": "system",
            "content": """You are trained to analyze and detect the sentiment of given text.
                                      if you are unsure of any answer, you can say "not sure"and recommend uses to review manually.""",
        },
        {
            "role": "user",
            "content": f"""Analyze the following text and determine if the sentiment is: positve or negative.
                                    Return answer in single word as either positive or negative: {text}""",
        },
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0,
    )

    # print(response)
    response_text = response.choices[0].message.content.strip().lower()

    return response_text


def sentiment(request):
    if request.method == "POST":
        message = request.POST.get("message")
        response = Sentiment_analysis(message)
        return JsonResponse({"message": message, "response": response})
    return render(request, "sentiment.html")
