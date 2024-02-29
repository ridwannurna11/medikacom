def print_menu():
    print("Berikut adalah daftar barang yang tersedia:")
    print("caffe americano: Rp37000.00 per cup")
    print("caramel macchiato: Rp59000.00 per cup")
    print("asian dolce latte: Rp55000.00 per cup")
    print("caramel latte: Rp52000.00 per cup")
    print("vanilla latte: Rp52000.00 per cup")
    print("caffe latte: Rp48000.00 per cup")
    print("cappuccino: Rp48000.00 per cup")
    print("caffe mocha: Rp55000.00 per cup")

def calculate_total(menu, order):
    total = 0
    for item, quantity in order.items():
        if item in menu:
            total += menu[item] * quantity
    return total

def apply_taxes(total, is_discount_applicable):
    tax_percent = 10
    if is_discount_applicable and total > 350000:
        discount_percent = 15
        total -= total * (discount_percent / 100)
    total += total * (tax_percent / 100)
    return total

def main():
    menu = {
        "caffe americano": 37000,
        "caramel macchiato": 59000,
        "asian dolce latte": 55000,
        "caramel latte": 52000,
        "vanilla latte": 52000,
        "caffe latte": 48000,
        "cappuccino": 48000,
        "caffe mocha": 55000
    }
    print_menu()
    order = {}
    while True:
        item = input("Masukkan pesanan anda (atau 'order' untuk selesai): ")
        if item.lower() == "order":
            break
        if item in menu:
            quantity = int(input(f"Berapa cup {item} yang anda inginkan? "))
            order[item] = order.get(item, 0) + quantity
    total = calculate_total(menu, order)
    tax_amount = apply_taxes(total, total > 350000)
    print(f"Total belanja anda adalah: Rp{total:,.0f}")
    print(f"PPN {10} %: Rp{tax_amount - total:,.0f}")
    print(f"Total belanja anda setelah pajak dan diskon: Rp{tax_amount:,.0f}")

if __name__ == "__main__":
    main()