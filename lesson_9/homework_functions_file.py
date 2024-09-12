def list_numbers_calculation(list_with_values: list):
    result = []
    for values in list_with_values:
        separate_list = values.split(',')
        # Try to make int from string, if exception occurred we will go to exception block
        try:
            value = [int(i) for i in separate_list]
        except ValueError as ve:
            result.append(f"I can't do it, {ve}")
        else:
            result.append(sum(value))
    return result


def count_product_price(products: list):
    list_prices = [x[1] * x[2] for x in products]
    total_price = sum(list_prices)
    return total_price


def count_total_price(once_payment: int, month: int):
    return once_payment * month


def required_album_pages(all_photos, photos_per_page):
    needed_pages = all_photos / photos_per_page
    return needed_pages


