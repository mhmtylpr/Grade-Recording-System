import colorama

#Secim menusu tasarımı
def menu():
    result1 = colorama.Fore.CYAN + "1)Not Oku"
    result2 = colorama.Fore.CYAN + "2)Not Gir"
    result3 = colorama.Fore.CYAN + "3)Not Çıkış"
    print(colorama.Fore.RED + f"""
    =====================================================================
    ''                                                                 ''
    ''                          {result1}                              ''
    ''                          {result2}                              ''
    ''                          {result3}                            ''
    ''                                                                 ''
    =====================================================================

    """)
menu()

#Not işlemleri için sınıf tanımlaması
class NotSystem:
    def __init__(self):
        pass
    def secim(self):
        sec = input(colorama.Fore.GREEN + ">>Hangi işlemi yapacaksınız: ")
        try:
            if int(sec) <4:
                sec = int(sec)
            else:
                print("3 ve 3 ten küçük bbir değer giriniz...")
        except:
            print("Ekranda yazılı seçimleri giriniz lütfem!!!")
        if sec == 1 :
            self.not_oku()
        elif sec == 2 :
            self.not_gir()
        else:
            self.cıkıs()
    #Not okuma metodu eklendi
    def not_oku(self):
        with open("Not.txt", "r", encoding="utf-8") as f:
            for i in f:
                print(colorama.Fore.WHITE + i, end="")
        self.finallysys()
    # Not ekleme metodu eklendi
    def not_gir(self):
        try:
            self.name = input("Adınız: ")
            self.not1 = input("Not-1: ")
            self.not1 = int(self.not1)
            self.not2 = input("Not-2: ")
            self.not2 = int(self.not2)
            self.not3 = input("Not-3: ")
            self.not3 = int(self.not3)

            if self.not1<=100 and self.not2<=100 and self.not3<=100:
                self.hesap(not1=self.not1, not2=self.not2, not3=self.not3, ısım=self.name)
                self.finallysys()
            else:
                print("Not kısmını 100 den küçük giriniz...(İşlemi tekrar yapınız!!)")
                self.finallysys()
        except:
            print("Lütfen not kısmına sayı giriniz")
            self.finallysys()

    #Çıkış metodu eklendi
    def cıkıs(self):
        pass
    #hesap metodu eklendi
    def hesap(self,not1,not2,not3,ısım):
        self.ortalama = (not1+not2+not3)/3
        if self.ortalama >=90:
            self.yazdır(ısım,"AA")
        elif self.ortalama<90 and self.ortalama>=80:
            self.yazdır(ısım, "BA")
        elif self.ortalama<80 and self.ortalama>=75:
            self.yazdır(ısım, "BB")
        elif self.ortalama<75 and self.ortalama>=70:
            self.yazdır(ısım, "CB")
        elif self.ortalama<70 and self.ortalama>=60:
            self.yazdır(ısım, "CC")
        elif self.ortalama<60 and self.ortalama>=50:
            self.yazdır(ısım, "DC")
        elif self.ortalama<50 and self.ortalama>=45:
            self.yazdır(ısım, "DD")
        else:
            self.yazdır(ısım, "FF")
        self.finallysys()

    #Notları bir txt metninie yazdırmak için gereki olan metod
    def yazdır(self,ısım,harfnotu):
        with open("Not.txt","a",encoding="utf-8") as f:
            character = f"{ısım}: {harfnotu}\n"
            f.write(character)

    #Sistemin sürekli bir döngü içerisinde çalıması sağlandı
    def finallysys(self):
        self.secim()

if __name__ == "__main__":
    NotSystem().finallysys()
