from tabulate import tabulate

class Transaction:
    def __init__(self) -> None:
        self.choice = None
        self.customer_cart = dict()
        pass
    
    def __choice_handler__(self):
        while True:
            try:
                choice = int(input('Masukkan Nomor Tugas : '))
                break  # Break out of the loop if the input is a valid integer
            except ValueError:
                print("Input harus berupa angka. Silakan coba lagi.")
            except Exception as e:
                print(e)
                return
            
        return choice

    def __delete_item__(self):
        item_name = input("Masukan Nama Barang yang ingin dihapus: ").lower()

        if item_name not in self.customer_cart:
            print("Barang tidak ada di keranjang. Ingin tambahkan ke keranjang?")
            print("1. Ya")
            print("2. Tidak")
            choice = self.__choice_handler__()
            if choice == 1:
                self.__add_item__(item_name)
            return

        self.customer_cart.pop(item_name)
        return
    
    def __reset_transaction__(self):
        print("Yakin menghapus semua keranjang?")
        print("1. Ya")
        print("2. Tidak")
        choice = self.__choice_handler__()
        if choice == 1:
            self.customer_cart = dict()
            print("Semua item berhasil di delete!")
        return
    
    def __update_item_name__(self):
        item_name = input ("Masukan Nama Barang yang ingin diupdate: ").lower()

        if item_name not in self.customer_cart:
            print("Barang tidak ada di keranjang. Ingin tambahkan ke keranjang?")
            print("1. Ya")
            print("2. Tidak")
            choice = self.__choice_handler__()
            if choice == 1:
                self.__add_item__(item_name)
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
        item_name = input ("Masukan Nama Barang yang diupdate:").lower()

        if item_name not in self.customer_cart:
            print("Barang tidak ada di keranjang. Ingin tambahkan ke keranjang?")
            print("1. Ya")
            print("2. Tidak")
            choice = self.__choice_handler__()
            if choice == 1:
                self.__add_item__(item_name)
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
        item_name = input ("Masukan Nama Barang yang diupdate: ").lower()

        if item_name not in self.customer_cart:
            print("Barang tidak ada di keranjang. Ingin tambahkan ke keranjang?")
            print("1. Ya")
            print("2. Tidak")
            choice = self.__choice_handler__()
            if choice == 1:
                self.__add_item__(item_name)
            return

        while True:
            try:
                item_price = int(input("Masukan Harga Barang: "))
                break  
            except ValueError:
                print("Input harus berupa angka. Silakan coba lagi.")

        self.customer_cart[item_name]['price'] = item_price
        return

    def __add_item__(self, item_name = None):
        """
        Fungsi untuk menambahkan barang.
        """
        if item_name == None:
            item_name = input ("Masukan Nama Barang: ").lower()
        while True:
            try:
                item_qty = int(input("Masukan Jumlah Barang: "))
                break  
            except ValueError:
                print("Input harus berupa angka. Silakan coba lagi.")
        while True:
            try:
                item_price = int(input("Masukan Harga Barang: "))
                break  
            except ValueError:
                print("Input harus berupa angka. Silakan coba lagi.")

        self.customer_cart.update({
            item_name : {
                "qty": item_qty,
                "price": item_price,
            },
        
        })

    def __check_order__(self):
        print("Daftar Belanjaan Anda")
        print("-"*60)
        self.__cart_list__()
        return
    
    def __checkout__(self):
        print("Daftar Belanjaan Anda")
        print("-"*60)
        self.__cart_list__()
        

        total_price = 0
        for key, v in self.customer_cart.items():
            total_price = total_price + (v['qty'] * v['price'])

        discount_1, discount_2, discount_3 = 5, 8, 10
        if total_price > 500_000:
            total_price = total_price * (100-discount_3)/100
        elif total_price > 300_000:
            total_price = total_price * (100-discount_2)/100
        elif total_price > 200_000:
            total_price = total_price * (100-discount_1)/100
    
        print(f"Total Belanja yang harus dibayarkan adalah Rp.{total_price},-")
        return 

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
        self.choice = self.__choice_handler__()
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
        elif choice == 7:
            self.__cart_list__()
        elif choice == 8:
            self.__checkout__()
            self.choice = 9
            return
        return 
    
    def display(self): 
        while self.choice != 9:
            self.list()
            self.action()

        print("""
            Thank you for using Super Cashier. See you next time ~
        ------------------------------------------------------
        """)

