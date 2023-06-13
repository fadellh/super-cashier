from tabulate import tabulate

class Transaction:
    def __init__(self) -> None:
        self.choice = None
        self.customer_cart = dict()
        pass
    
    def __delete_item__(self):
        item_name = input ("Masukan Nama Barang yang ingin dihapus: ")

        if item_name not in self.customer_cart:
            print("Barang tidak ada di keranjang. Ingin tambahkan ke keranjang?")
            print("1. Ya")
            print("2. Tidak")
            choice = int(input('Masukkan Nomor Tugas : '))
            if choice == 1:
                self.__add_item__()
            return

        self.customer_cart.pop(item_name)
        return
    
    def __reset_transaction__(self):
        self.customer_cart = dict()
        return
    
    def __update_item_name__(self):
        item_name = input ("Masukan Nama Barang yang ingin diupdate: ")

        if item_name not in self.customer_cart:
            print("Barang tidak ada di keranjang. Ingin tambahkan ke keranjang?")
            print("1. Ya")
            print("2. Tidak")
            choice = int(input('Masukkan Nomor Tugas : '))
            if choice == 1:
                self.__add_item__()
            return

        while True:
            item_name_update = input("Masukan Nama Item Baru: ")
            break
     
        current_data = self.customer_cart[item_name]
        self.customer_cart.pop(item_name)
        self.customer_cart.update({
            item_name_update : current_data
        })
        return
    
    def __update_item_qty__(self):
        item_name = input ("Masukan Nama Barang yang diupdate:")

        if item_name not in self.customer_cart:
            print("Barang tidak ada di keranjang. Ingin tambahkan ke keranjang?")
            print("1. Ya")
            print("2. Tidak")
            choice = int(input('Masukkan Nomor Tugas : '))
            if choice == 1:
                self.__add_item__()
            return

        while True:
            try:
                item_qty = int(input("Masukan Jumlah Barang: "))
                break  # Break out of the loop if the input is a valid integer
            except ValueError:
                print("Input harus berupa angka. Silakan coba lagi.")

        self.customer_cart[item_name]['qty'] = item_qty
        return
    
    def __update_item_price__(self):
        item_name = input ("Masukan Nama Barang yang diupdate:")

        if item_name not in self.customer_cart:
            print("Barang tidak ada di keranjang. Ingin tambahkan ke keranjang?")
            print("1. Ya")
            print("2. Tidak")
            choice = int(input('Masukkan Nomor Tugas : '))
            if choice == 1:
                self.__add_item__()
            return

        while True:
            try:
                item_price = int(input("Masukan Harga Barang:"))
                break  # Break out of the loop if the input is a valid integer
            except ValueError:
                print("Input harus berupa angka. Silakan coba lagi.")

        self.customer_cart[item_name]['price'] = item_price
        return

    def __add_item__(self):
        """
        Fungsi untuk menambahkan barang.
        """
        item_name = input ("Masukan Nama Barang:")
        while True:
            try:
                item_qty = int(input("Masukan Jumlah Barang: "))
                break  # Break out of the loop if the input is a valid integer
            except ValueError:
                print("Input harus berupa angka. Silakan coba lagi.")
        while True:
            try:
                item_price = int(input("Masukan Harga Barang:"))
                break  # Break out of the loop if the input is a valid integer
            except ValueError:
                print("Input harus berupa angka. Silakan coba lagi.")

        # item = dict()
        self.customer_cart.update({
            item_name : {
                "qty": item_qty,
                "price": item_price,
            },
        
        })

    def __cart_list__(self):
        table_data = []

        idx = 0
        for key, v in self.customer_cart.items():
            if idx == 0:
                table_data.append(["Item", "Jumlah Item", "Harga/Item", "Harga Total"])

            item_name = key
            item_qty = v["qty"]
            item_price = v["price"]
            total_price = item_price * item_qty
            table_data.append([item_name, item_qty, item_price, total_price])
            idx += 1

        table = tabulate(table_data, headers="firstrow", tablefmt="fancy_grid")
        print(table)

    def list(self):
        """
        Fungsi untuk menampilkan pilihan action oleh user.
        """
        print("-"*60)
        if len(self.customer_cart) == 0:
            print("SELAMAT DATANG DI SUPERMARKET ANDI, INI ADALAH LAYANAN KASIR SELF SERVICE")
        else:
            print("Daftar Belanjaan Anda")
            self.__cart_list__()
        print("-"*60)
        print("1. Tambahkan item yang ingin di beli")
        if len(self.customer_cart) > 0:
            print("2. Perbarui nama item")
            print("3. Perbarui jumlah item")
            print("4. Perbarui harga item")
            print("5. Menghapus salah satu item")
            print("6. Menghapus item keseluruhan")
            print("7. Perikasa transaksi")
            print("8. Checkout")
        print("9. Exit\n")
        return 

    def action(self):
        self.choice = int(input('Masukkan Nomor Tugas : '))
        choice = self.choice
        if choice == 1:
            self.__add_item__()
        elif choice == 2:
            self.__update_item_name__()
        elif choice == 3:
            self.__update_item_qty__()
        elif choice == 4:
            self.__update_item_price__()
        elif choice == 5:
            self.__delete_item__()
        elif choice == 6:
            self.__reset_transaction__()
        return 
    
    def display(self): 
        while self.choice != 9:
            self.list()
            self.action()

        print("""
            Thank you for using Super Cashier. See you next time ~
        ------------------------------------------------------
        """)

