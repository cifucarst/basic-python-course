#!/usr/bin/env/ python3

# project

games = ["Super Mario Bros", "Zelda: Breath of the Wild", "Cyberpunk 2077", "Final Fantasy VII"]
threshold = 500

# genres
genres = {
    "Super Mario Bros": "Adventure",
    "Zelda: Breath of the Wild": "Adventure",
    "Cyberpunk 2077": "Role-Playing",
    "Final Fantasy VII": "Role-Playing",
}

# sales and stock
sales_and_stock = {
    "Super Mario Bros": (400, 200),
    "Zelda: Breath of the Wild": (600, 20),
    "Cyberpunk 2077": (60, 120),
    "Final Fantasy VII": (924, 3),
}

# customers
customers = {
    "Super Mario Bros": {"marcelo", "hackermate", "hackavis", "securiters", "lobotec"},
    "Zelda: Breath of the Wild": {"hackermate", "hackavis", "lucia", "manolo", "pepe"},
    "Cyberpunk 2077": {"hackermate", "lobotec", "pepe", "raquel", "albert"},
    "Final Fantasy VII": {"lucia", "manolo", "pepe", "securiters", "patricia", "moises"},
}

# my_game = "Super Mario Bros"
def summary(game):
    # summary
    print(f'\n[i] Game Summary: {game}\n')
    print(f'\t[+] Genre: {genres[game]}')
    print(f'\t[+] Total sales for this game: {sales_and_stock[game][0]} units')
    print(f'\t[+] Total stock for this game: {sales_and_stock[game][1]} units')
    print(f"\t[+] Customers who have purchased the game: {', '.join(customers[game])}")

for game in games:
    if sales_and_stock[game][0] > threshold:
        summary(game)

total_sales = lambda: sum(ventas for game, (ventas, _) in sales_and_stock.items() if sales_and_stock[game][0] > threshold)

print(f"\n[+] The total sales of all products have been {total_sales()} units")
