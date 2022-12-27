```hayvan kedi köpek kuş papağan karga şahin ile oop kodu yazın

hayvan classında herkesin ismi olsun zorunlu olsun eğer istenirse 2. isim eklenebilinir olsun
hayvan classı hepsinin atası olucak
ve hayvan classında ses_cıkart adında bir method olsun ve notImplementedError atsın

kedi classi ses_cıkart methodunu override etsin miyavv yazdırsın

kopek classı da ses_cıkart methodunu override etsin hav yazdırsın
ayrıca köpek classının ısır diye bir methodu olsun bu method başka bir hayvanı parametre olarak alsın
sonra "diğer_hayvan_ismi yi ısrdım" diye print etsin

kuş classı da ses_cıkart ı override etsin cik yazdırsın ekrana
ayrıca kaç tane kuş oluştuğunu yazdığı bir method olsun adı da kac_kus_var olsun
3 papağan 2 karga 3 şahin varsa 7 kuş yazmalı yani

papağan classı kuş classını inherit etsin. ses_cıkart methodunu override etsin ve bu sefer bir string parametresi alsın
ve "gaak input_string" ekrana bastırsın
ayrıca papağan classının bir de renk değişkeni olsun girilmesi zorunlu olsun _init_ de verilsin

şahin classı nda avlanıyorum diye bir method olsun
ama sadece kedi  avlayabilsin köpek ve kuşsa avlayamasın
kediyse ismini yazdırıp avladım yazdırsın
kuş ve köpekse bunu avlayamam yazdırsın```






class Hayvan:
    def __init__(self, isim, ikinci_isim=None):
        self.isim = isim
        self.ikinci_isim = ikinci_isim
    
    def ses_cikart(self):
        raise NotImplementedError

class Kedi(Hayvan):
    def ses_cikart(self):
        print("miyav")

class Kopek(Hayvan):
    def ses_cikart(self):
        print("hav")
    
    def isir(self, hayvan):
        print(f"{hayvan.isim} yi ısırdım")

class Kus(Hayvan):
    sayac = 0
    
    def __init__(self, isim, ikinci_isim=None):
        super().__init__(isim, ikinci_isim)
        Kus.sayac += 1
    
    def ses_cikart(self):
        print("cik")
    
    def kac_kus_var(cls):
        return cls.sayac

class Papagan(Kus):
    def __init__(self, isim, renk, ikinci_isim=None):
        super().__init__(isim, ikinci_isim)
        self.renk = renk
    
    def ses_cikart(self, string):
        print(f"gaak {string}")

class Sahin(Kus):
    def avlaniyorum(self, hayvan):
        if isinstance(hayvan, Kedi):
            print(f"{hayvan.isim} avladım")
        elif isinstance(hayvan, (Kopek, Kus)):
            print("bu hayvanı avlayamam")

kedi1 = Kedi("Tom")
kedi1.ses_cikart()

kopek1 = Kopek("vudi")
kopek1.ses_cikart()
kopek1.isir(kedi1)

kus1 = Kus("Twiti")
print(Kus.sayac)
kus1.ses_cikart()

kus2 = Kus("çapkın")
print(Kus.sayac)
kus3 = Kus("Selam")

papagan1 = Papagan("Fatik","Sarı","Özbay")
print(papagan1.isim,papagan1.renk,papagan1.ikinci_isim)
papagan1.ses_cikart("ALOOOOOOO")

Sahin1 = Sahin("muzaffer")
Sahin1.avlaniyorum(kedi1)
Sahin1.avlaniyorum(kus1)
Sahin1.ses_cikart()
print(Kus.sayac)