import csv
from datetime import datetime

# Daftar film yang tersedia
films = [
    {"title": "Film Ambacong", "showtime": "23:00", "price": 100000},
    {"title": "Film Rainbow Rusdy", "showtime": "21:00", "price": 6000000},
    {"title": "Film Suster ngakak", "showtime": "19:00", "price": 70000000},
]

def display_films():
    print("Daftar Film:")
    for idx, film in enumerate(films):
        print(f"{idx + 1}. {film['title']} - Jam Tayang: {film['showtime']} - Harga: Rp{film['price']}")

def book_ticket():
    display_films()
    
    # Memilih film
    film_choice = int(input("Pilih film (nomor): ")) - 1
    if film_choice < 0 or film_choice >= len(films):
        print("Pilihan tidak valid.")
        return
    # Memasukkan jumlah tiket
    num_tickets = int(input("Masukkan jumlah tiket: "))
    
    # Menghitung total harga
    total_price = num_tickets * films[film_choice]["price"]
    print(f"Total Harga: Rp{total_price}")
    
    # Menyimpan riwayat pemesanan
    save_booking(films[film_choice]["title"], num_tickets, films[film_choice]["showtime"], total_price)

def save_booking(title, num_tickets, showtime, total_price):
    with open('booking_history.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), title, num_tickets, showtime, total_price])
    print("Riwayat pemesanan telah disimpan.")

if __name__ == "__main__":
    while True:
        book_ticket()
        another = input("Ingin memesan tiket lagi? (y/n): ")
        if another.lower() != 'y':
            break
    