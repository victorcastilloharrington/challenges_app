from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
# Create your views here

monthly_challenges = {
    'january': 'Happy january',
    'february': 'Happy february',
    'march': 'Happy march',
    'april': 'Happy april',
    'may': 'Happy may',
    'june': 'Happy june',
    'july': 'Happy july',
    'august': 'Happy august',
    'september': 'Happy september',
    'october': 'Happy october',
    'november': 'Happy november',
    'december': 'Happy december',
}


def index(request):
    months = list(monthly_challenges.keys())
    result_months = ''
    for month in months:
        capitalized_month = month.capitalize()
        result_months = result_months + \
            f'<li><a href="{month}">{capitalized_month}</a></li>'

    response_data = f'<ul>{result_months}</ul>'

    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):

    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Month not supported")

    redirect_month = months[month - 1]
    return HttpResponseRedirect(redirect_month)


def monthly_challenge(request, month):
    # try:
    challenge_text = monthly_challenges[month]
    challenge_data = render_to_string(
        'challenges/challenge.html')
    return HttpResponse(challenge_data)
    # except:
    return HttpResponseNotFound('Month not supported')
