import socket, random, time
print('''

░█████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗
██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝
██║░░╚═╝███████║███████║██║░░╚═╝█████═╝░█████╗░░
██║░░██╗██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░
╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝

██╗███╗░░██╗░██████╗████████╗░█████╗░
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗
██║██╔██╗██║╚█████╗░░░░██║░░░███████║
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝
 
|=================================================|
|      [ + ] by kavani                            |
|=================================================|
|      [ + ] Instagram : 2knn01                   |                   
|=================================================|
|      [ + ] Telegram : https://t.me/kavani2knn10 |                   
|=================================================| 

==========================================
- four letters [1]\n  
- five letters [2]\n
==========================================
''')
choose = input("please choose option : ") 
if choose == '1':
         while True:
          A = "abcdefghijkImnopqrstuvwxyz"
          a = "123456789"
          all=A + a 
          length1 = 4    
          user ="".join(random.sample(all,length1))
          print(""+user)
          time.sleep(0.7)

if choose == '2':
     while True:
          A = "abcdefghijkImnopqrstuvwxyz"
          a = "123456789"
          all=A + a 
          length1 = 5    
          user ="".join(random.sample(all,length1))
          print(""+user)
          time.sleep(0.7)
