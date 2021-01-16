import requests
response = requests.get('https://docs.google.com/forms/d/e/1FAIpQLScyX3y0WpM6GrBHYsc8mlzAU3loR3xLgIOouIq5rL34oE7ZbA/viewform?usp=sf_link')
assert response.status_code == 200, 'Wrong status code'
print(response.content)
