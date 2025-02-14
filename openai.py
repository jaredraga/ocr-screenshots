import openai
from constants import APIKEY
openai.api_key = APIKEY

ocrtext = """
Your program should first prompt the user for a starting population size.

    If the user enters a number less than 9 (the minimum allowed population size), the user should be re-prompted to enter a starting population size until they enter a number that is greater than or equal to 9. (If we start with fewer than 9 llamas, the population of llamas will quickly become stagnant!)

Your program should then prompt the user for an ending population size.

    If the user enters a number less than the starting population size, the user should be re-prompted to enter an ending population size until they enter a number that is greater than or equal to the starting population size. (After all, we want the population of llamas to grow!)

"""

output = openai.chatcompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "You classify text that will be given to you using single words. The words must be from fields of work of society like programming, self defense, psychology, etc."},
        {"role": "user", "content": ocrtext}
    ]
)

print(output)