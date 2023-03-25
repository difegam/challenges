import calendar

from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

challenges = {
    "january": "Write a program that prints the Fibonacci sequence up to 1000.",
    "february": "Write a program that checks if a given string is a palindrome.",
    "march": "Write a program that calculates the area of a circle given its radius.",
    "april": "Write a program that simulates a game of rock-paper-scissors against the computer.",
    "may": "Write a program that generates a random password of a given length.",
    "june": "Write a program that calculates the prime factors of a given number.",
    "july": "Write a program that counts the number of words in a given text file.",
    "august": "Write a program that simulates a game of tic-tac-toe against the computer.",
    "september": "Write a program that generates a list of all the prime numbers up to a given number.",
    "october": "Write a program that calculates the factorial of a given number.",
    "november": "Write a program that calculates the sum of the digits of a given number.",
    "december": "Write a program that converts a given temperature from Celsius to Fahrenheit.",
    "test": None,
}


def monthly_challenge_by_number(request, month: int):

    if month <= 0 or month > len(calendar.month_name):
        return HttpResponseNotFound(f"Please enter a valid month. {month} in not supported")

    redirect_path_str = calendar.month_name[month].lower()
    redirect_path = reverse("month-challenge-str", args=[redirect_path_str])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges_list(request):
    months = challenges.keys()
    return render(request, "monthly/index.html", context={"months": months})


def monthly_challenge(request, month: str):
    challenge = challenges.get(month.lower())

    if not challenge:
        return HttpResponseNotFound(f"Please enter a valid month. {month} in not supported")

    context = {"month": month, "challenge": challenge}

    return render(request, "monthly/monthly_challenge.html", context=context)
