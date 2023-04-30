# PelaajaAPI
Backend kurssin lopputyö

Luotu käyttämällä Python versiota 3.11.1

## Käynnistysohjeet:
1. Avaa Git Bash. Siirry directoryyn mihin haluat kloonata repon ja kopioi teksti:
```
git clone https://github.com/MariaSaa/PelaajaAPI.git 
```
4. Avaa kopioitu repo koodieditoriin
5. Luo virtual enviroment (venv)
    
    a. Visual studio codessa command palette (Ctrl + Shift + P)
    
    b. Python: Create virtual enviroment
    
    c. Vaihtoehdoista _Venv or Conda_, valitse Venv
    
    d. Valitse Python versio ja enter
    
3. tarkista että luomasi venv on myös käynnissä. Jossei käynnisty automaattisesti, syötä alla oleva rimpsu terminaaliin projekti kansiossa:
```
.venv/Scripts/Activate.ps1
```

5. Asenna FastAPI:
```
pip install fastapi uvicorn
```
7. Asenna Sqlalchemy: 
```
pip install sqlalchemy
```
6. Käynnistä
```
uvicorn app.main:app --reload
```
7. Klikkaa linkkiä ja lisää _/docs_ jolloin dokumentaatio aukeaa 

