from pyscript import display, document

# Creating the receipt

def create_order(e):
    document.getElementById("result").innerHTML = " "
    prod1 = document.getElementById("chicken")
    prod2 = document.getElementById("sidedish")
    prod3 = document.getElementById("soda")

    subtotal = float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked
    display(f'The subtotal is ₱{subtotal:.2f}', target="result")

    vat_number = subtotal * 0.12
    display(f'The VAT is ₱{vat_number:.2f}', target="result")

    total_amount = subtotal + vat_number
    display(f'The total amount is ₱{total_amount:.2f}', target="result")

# Creating the SKU generator

def generate_sku(e):

    category = document.getElementById("category")
    product = document.getElementById("product")
    stock = document.getElementById("stock")

    category_code = category.value
    product_name = product.value
    stock_quantity = stock.value

    product_code = product_name.upper()
    product_code = product_code.replace(" ", "")
    product_code = product_code[:4]

    sku = category_code + "-" + product_code + "-" + stock_quantity

    document.getElementById("result").textContent = sku
