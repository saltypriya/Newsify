from newsapi import NewsApiClient
import pycountry
newsapi = NewsApiClient(api_key='b5a1d168eda24bf38f1feb48a659a02c')

input_country = input("Country: ")
input_countries = [f'{input_country.strip()}']
countries = {}
print(f"You have now selected:{input_country}")
option1=input("Want to search? Yes/No ::")
lis1=["Business".lower(),"Entertainment".lower(),"General".lower(),"Health".lower(),"Science".lower(),"Technology".lower()]
while option1=="Yes" or option1=="yes":
    for country in pycountry.countries:

        countries[country.name] = country.alpha_2


    codes = [countries.get(country.title(), 'Unknown code')
            for country in input_countries]


    option = input("Which category are you interested in?\n1.Business\n2.Entertainment\n3.General\n4.Health\n5.Science\n6.Technology\n\nEnter here: ")
    
    top_headlines = newsapi.get_top_headlines(

        
        category=f'{option.lower()}', language='en', country=f'{codes[0].lower()}')

    Headlines = top_headlines['articles']


    if Headlines:
            for articles in Headlines:
                b = articles['title'][::-1].index("-")
                if "news" in (articles['title'][-b+1:]).lower():
                    print(f"{Headlines.index(articles)+1}. {articles['title'][-b+1:]}: {articles['title'][:-b-2]}.")
                else:
                    print(f"{Headlines.index(articles)+1}. {articles['title'][-b+1:]} News: {articles['title'][:-b-2]}.")
                print()
    else:
        print(
            f"Sorry no articles found for {input_country}, Something Wrong!!!")
    option1 = input("Do you want to search again[Yes/No]? ")