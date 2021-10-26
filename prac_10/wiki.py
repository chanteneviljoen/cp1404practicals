import wikipedia


user_search_input = input('Enter page title / search phrase: ')
while user_search_input != '':
    try:
        page = wikipedia.page(user_search_input)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print('Please enter a more specific search phrase, such as:')
        for option in e.options[:5]:
            print(option)
    except wikipedia.exceptions.PageError:
        print('Page does not exist')
    user_search_input = input('Enter page title / search phrase: ')