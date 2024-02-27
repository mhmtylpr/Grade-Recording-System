import customtkinter
import tkinter
import os
from PIL import ImageTk, Image

class Not_GUI:
    def __init__(self):
        self.app=customtkinter.CTk()
        self.app.geometry("450x600")
        self.app.title("Not Kayıt Sistemi")
        self.app.iconbitmap("notes.ico")
        self.app.maxsize(width=450,
                         height=600)
        self.app.minsize(width=450,
                         height=600)
        self.frame = customtkinter.CTkFrame(master=self.app,
                                            width=430,
                                            height=570,
                                            corner_radius=14)
        self.frame.place(relx=0.5,
                         rely=0.5,
                         anchor=customtkinter.CENTER)
        self.users_Entry()
        self.button_factory()
        self.ımg_fr()
        self.app.mainloop()
    def users_Entry(self):
        self.name = customtkinter.CTkEntry(master=self.frame,
                                           width=240,
                                           height=40,
                                           placeholder_text="İsminizi Giriniz",
                                           border_width=0,
                                           font=("Microsoft YaHei",14,"normal"))
        self.name.place(relx=0.5,
                        rely=0.3,
                        anchor=customtkinter.CENTER)
        self.not1 = customtkinter.CTkEntry(master=self.frame,
                                           width=60,
                                           height=40,
                                           placeholder_text="Not 1",
                                           border_width=0,
                                           font=("Microsoft YaHei",14,"normal"))
        self.not1.place(relx=0.35,
                        rely=0.4,
                        anchor=customtkinter.CENTER)
        self.not2 = customtkinter.CTkEntry(master=self.frame,
                                           width=60,
                                           height=40,
                                           placeholder_text="Not 2",
                                           border_width=0,
                                           font=("Microsoft YaHei",14,"normal"))
        self.not2.place(relx=0.5,
                        rely=0.4,
                        anchor=customtkinter.CENTER)
        self.not3 = customtkinter.CTkEntry(master=self.frame,
                                           width=60,
                                           height=40,
                                           placeholder_text="Not 3",
                                           border_width=0,
                                           font=("Microsoft YaHei",14,"normal"))
        self.not3.place(relx=0.65,
                        rely=0.4,
                        anchor=customtkinter.CENTER)



    def button_factory(self):
        button_result = customtkinter.CTkButton(master=self.frame,
                                                text_color="white",
                                                fg_color="grey",
                                                text="Kayıt",
                                                width=120,
                                                font=("Microsoft YaHei",15,"normal"),
                                                hover_color="black",
                                                command=self.calıstır
                                                )

        button_result.place(relx=0.5,
                            rely=0.6,
                            anchor=customtkinter.CENTER)

        read_fuc = customtkinter.CTkButton(master=self.frame,
                                                text_color="white",
                                                fg_color="grey",
                                                text="Oku",
                                                width=80,
                                                font=("Microsoft YaHei",15,"normal"),
                                                hover_color="black",
                                                command=self.read_not)

        read_fuc.place(relx=0.5,
                       rely=0.7,
                       anchor=customtkinter.CENTER)

    def read_not(self):
        os.system("Not_list.txt")

    def result(self, not1, not2, not3, ısım):
        self.ortalama = (not1 + not2 + not3) / 3
        if self.ortalama >= 90:
            self.yazdır(ısım, "AA")
        elif self.ortalama < 90 and self.ortalama >= 80:
            self.yazdır(ısım, "BA")
        elif self.ortalama < 80 and self.ortalama >= 75:
            self.yazdır(ısım, "BB")
        elif self.ortalama < 75 and self.ortalama >= 70:
            self.yazdır(ısım, "CB")
        elif self.ortalama < 70 and self.ortalama >= 60:
            self.yazdır(ısım, "CC")
        elif self.ortalama < 60 and self.ortalama >= 50:
            self.yazdır(ısım, "DC")
        elif self.ortalama < 50 and self.ortalama >= 45:
            self.yazdır(ısım, "DD")
        else:
            self.yazdır(ısım, "FF")

    def yazdır(self, ısım, harfnotu):
        with open("Not_list.txt", "a", encoding="utf-8") as f:
            character = f"{ısım}: {harfnotu}\n"
            f.write(character)
        self.not1.delete(0,"end")
        self.not2.delete(0,"end")
        self.not3.delete(0,"end")
        self.name.delete(0,"end")

    def calıstır(self):

        try:
            try:
                name = self.name.get()
                not1 = int(self.not1.get())
                not2 = int(self.not2.get())
                not3 = int(self.not3.get())
                try:
                    if not1<=100 and not2<=100 and not3<=100:
                        self.result(not1, not2, not3, name)
                    else:

                        self.lab = customtkinter.CTkLabel(master=self.frame,
                                                          font=("Microsoft YaHei", 16, "normal"),
                                                          text_color="grey",
                                                          text="not 100 den büyük olacak")
                        self.lab.place(relx=0.5,
                                       rely=0.8,
                                       anchor=tkinter.CENTER)

                except:
                    pass

            except:

                self.lab = customtkinter.CTkLabel(master=self.frame,
                                                  font=("Microsoft YaHei", 16, "normal"),
                                                  text_color="grey",
                                                  text="not kısmına Sayı gir")
                self.lab.place(relx=0.5,
                               rely=0.8,
                               anchor=tkinter.CENTER)
        except:
            pass

    def ımg_fr(self):
        self.image_path = os.path.join(os.path.dirname(__file__),"notes.png")
        self.image = customtkinter.CTkImage(light_image=Image.open(self.image_path),
                                       size=(80,80)
                                       )

        self.image_label = customtkinter.CTkLabel(master=self.frame,
                                             image=self.image,
                                             text=" "
                                             )
        self.image_label.place(relx=0.5,
                          rely=0.15,
                          anchor=customtkinter.CENTER
                          )


        # Open function ile ya dosya açlacak ya da ekrana textbox,label ile yazdırılacak

if __name__=="__main__":
    Not_GUI()