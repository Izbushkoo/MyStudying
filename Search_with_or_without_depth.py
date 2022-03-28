site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search(site, key, *args):
    if key in site:
        return site[key]
    for sub_site in site.values():
        if isinstance(sub_site, dict) and len(args) == 2:
            real_depth, depth = args
            if real_depth <= depth:
                result = search(sub_site, key, real_depth + 1, depth)
                if result:
                    break
        elif isinstance(sub_site, dict):
            result = search(sub_site, key)
            if result:
                break
    else:
        result = None
    return result


def ask(question):
    answer = input(question).lower()
    if answer == "y":
        real_depth = 2
        depth = int(input("Enter the depth: "))
        print("Key value:", search(site, key, real_depth, depth))
    elif answer == "n":
        print("Key value:", search(site, key))


key = input("Enter searched key: ")
ask("Want to enter a depth? Y/N: ")


