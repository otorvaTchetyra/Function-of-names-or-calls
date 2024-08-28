calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    global calls
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    global calls
    count_calls()
    return any(string.lower() in s.lower() for s in list_to_search)

# Вызовем функции с произвольными данными
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)