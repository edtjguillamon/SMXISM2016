# ***Sistemes RAID*** 

## 1. **Resum de sistemes RAID fent servir una taula com la vista a classe**

|   Nivells |   Nº Min Discs |   Nº Max Fail |  Capacitat  |  Read  |  Write  |
| --------- | -------------- | ------------- | ----------- | ------ | ------- | 
|   Raid 0  |        2       |       0       |      100%   |  Exc.  |   Exc.  |
|   Raid 1  |     2 (Màx)    |       1       |       50%   |  M.Bé  |    Bé   |  
|   Raid 5  |        3       |       1       |    67-94%   |  M.Bé  |    Bé   | 		
|   Raid 6  |        4       |       2       |    50-88%   |  Bé    |    Bé   | 		  
|   Raid 10 |        4       |   1/mirror    |       50%   |  M.Bé  |    Bé   | 		  

## 2. **Comandes i descripció de les mateixes per tal de crear un sistema RAID1**

*Mmdadm --create <nom_dispositiu> --level=1 --raid-devices=2 <DD1> <DD2>*
**Definim el nom del dispositiu RAID, el nivell en el qual l'establim, el numero
discs durs que afegim i després el nom de cada disc dur.**

*mkfs.ext4 /dev/md1*
**Creem el sistema de fitxers ext4 i l'afegim al dispositiu RAID.** 

*mount /dev/md1 /mnt* 
**Montem el dispositiu RAID a la carpeta /mnt** 

## 3. **Comandes i descripció de les mateixes per tal de crear un sistema RAID5**

*Mmdadm --create <nom_dispositiu> --level=5 --raid-devices=3 <DD1> <DD2> <DD3>*
**Definim el nom del dispositiu RAID, el nivell en el qual l'establim, el numero
discs durs que afegim i després el nom de cada disc dur.**

*mkfs.ext4 /dev/md5*
**Creem el sistema de fitxers ext4 i l'afegim al dispositiu RAID.**

*mount /dev/md5 /mnt*
**Montem el dispositiu RAID a la carpeta /mnt** 

## 4. **Comandes i descripció de les mateixes per tal de crear un sistema RAID6**

*Mmdadm --create <nom_dispositiu> --level=6 --raid-devices=4 <DD1> <DD2> <DD3> <DD4>*
**Definim el nom del dispositiu RAID, el nivell en el qual l'establim, el numero
discs durs que afegim i després el nom de cada disc dur.**

*mkfs.ext4 /dev/md6*
**Creem el sistema de fitxers ext4 i l'afegim al dispositiu RAID.**

*mount /dev/md6 /mnt*
**Montem el dispositiu RAID a la carpeta /mnt** 

## 5. **Comandes i descripció de les mateixes per tal de crear un sistema RAID10**

*Mmdadm --create <nom_dispositiu> --level=10 --raid-devices=4 <DD1> <DD2> <DD3> <DD4>*
**Definim el nom del dispositiu RAID, el nivell en el qual l'establim, el numero
discs durs que afegim i després el nom de cada disc dur.**

*mkfs.ext4 /dev/md10*
**Creem el sistema de fitxers ext4 i l'afegim al dispositiu RAID.**

*mount /dev/md10 /mnt*
**Montem el dispositiu RAID a la carpeta /mnt** 
