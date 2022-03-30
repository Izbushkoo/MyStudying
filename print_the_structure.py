def product_site(product):

    # Here we have an example data-structure in where we want to change some part into different one.
    # So we use string format method.

    site = {
        'html': {
            'head': {
                'title': 'Куплю/продам {product} недорого'.format(product=product)
            },
            'body': {
                'h2': 'У нас самая низкая цена на {product}'.format(product=product),
                'div': 'Купить',
                'p': 'продать'
            }
        }
    }

    return site


def print_of_structure_1(data, tabs):

    # It is the part of printing the structure.
    # Variable "tabs" in charge of literal tabulations number, that will increase by two with
    # every level of structure.

    if not isinstance(data, dict):
        # here is basic part of function that will initialize
        # the exit if given data is not a dictionary.
        return 0
    str_tabs = '\t' * tabs
    for elem, value in data.items():
        str_tabs = '\t' * tabs
        if not isinstance(value, dict):
            print(str_tabs + f"'{elem}': '{value}'")
        else:
            print(str_tabs + f"'{elem}':", "{")
            print_of_structure_1(value, tabs + 2)
    print(str_tabs + '}')


def structure(num, product_list):

    # This part is responsible for asking the number of changes and creating a list of them.
    # The goal is to print every time after changing all the previous structures.

    if num == 0:
        return

    product = input("Enter product name for new site: ")
    product_list.append(product)


    for item in product_list:
        print(f'Site for {item}:')
        print('site =', '{')
        print_of_structure_1(product_site(item), 2)
    structure(num - 1, product_list)


# And the main part of code I hope understandable one.


product_list = []
number_of_sites = int(input("Enter number of sites: "))
structure(number_of_sites, product_list)

