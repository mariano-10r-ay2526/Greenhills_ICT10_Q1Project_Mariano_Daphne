from pyscript import display, document

# Creating the receipt
def create_order(e):
    document.getElementById("result").innerHTML = ""

    prod1 = document.getElementById("chicken")
    prod2 = document.getElementById("sidedish")
    prod3 = document.getElementById("soda")

    subtotal = (float(prod1.value) * prod1.checked) + \
               (float(prod2.value) * prod2.checked) + \
               (float(prod3.value) * prod3.checked)

    vat_number = subtotal * 0.12
    total_amount = subtotal + vat_number

    text = (
        f"Your subtotal is ₱{subtotal:.2f}\n"
        f"Your VAT is ₱{vat_number:.2f}\n"
        f"Your total amount is ₱{total_amount:.2f}"
    )

    display(text, target="result")

# Creating SKU
def generate_sku(e):

    category = document.getElementById("category")
    product = document.getElementById("product")
    stock = document.getElementById("stock")
    result_div = document.getElementById("result")

    if not stock.value:
        result_div.textContent = "Please enter a stock quantity."
        return

    category_code = category.value
    product_name = product.value
    stock_quantity = stock.value

    product_code = product_name.upper().replace(" ", "")[:4]

    sku = f"{category_code}-{product_code}-{stock_quantity}"
    result_div.textContent = sku