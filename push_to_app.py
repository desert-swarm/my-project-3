import requests 

if __name__=='__main__':
    url = 'http://127.0.0.1:5000/product-create'

    # requests.post(url, data={'name':'iPhone', 'price':'549.0'})

    data_db_app2 = {'name': 'iPhone 5S', 'price': '549.0', 'category': 'Phones'}
    requests.post(url, data=data_db_app2)