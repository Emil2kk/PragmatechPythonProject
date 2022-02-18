name=input()
if len(name)>3 and len(name)<11:
    print("ad duzgun daxil edildi")
    surname=input()
    if len(surname)>5 and len(surname)<15:
        print("soyad duzgun daxil edildi")
        email=input()
        if len(email)>10 and len(email)<22 and "@gmail.com" in email:
            print("email duzgun daxil edildi")
            password=input()
            if len(password)>6 and len(password)<13 :
                print("passwordunuzu tesdiqleyin")
                pasSword=input()
                if password== pasSword :
                    print("qeydiyyat tamamlandi")
                    quest=input("detallara baxmaq isteyirsiz? yes or no")
                    if quest=="yes" :
                        print(f'ad:{name}, soyad: {surname}, email: {email}, password: {password} ')
                    else:
                        print(f'ad:{ad}, soyad: {soyad},Ugurlar')
                else:
                    print("password tesdiq olunmadi")
            else:
                print("simvol sayi 6 -13 arasinda olmalidi")
                
        else:
            print("email duzgun daxil edilmemisdir")
            
    else:
        print("soyad duzgun daxil edilmemisdir")
else:
    print("ad duzgun daxil edilmemisdir")