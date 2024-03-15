# class CartMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         response = self.get_response(request)
#         return response
#
#     def process_template_response(self, request, response):
#         my_cart = request.session.get('cart', [])
#
#         items_count = 0
#         for item in my_cart:
#             items_count += item['quantity']
#         response.context_data['items_count'] = items_count
#         return response

def cart_items_count(request):
    my_cart = request.session.get('cart', [])  # [{"product": 1, "quantity": 2}, {"product": 3, "quantity": 5}]
    #  request.session['cart'] -> [{"product": 1, "quantity": 2}, {"product": 3, "quantity": 5}]


    items_count = 0
    for item in my_cart:
        items_count += item['quantity']

    return {'items_count': items_count}