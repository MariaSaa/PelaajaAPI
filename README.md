# PelaajaAPI
Backend kurssin lopputyö

Luotu käyttämällä Python versiota 3.11.1

## Käynnistysohjeet:
1. Avaa Git Bash. Siirry directoryyn mihin haluat kloonata repon ja kopioi teksti:
```
git clone https://github.com/MariaSaa/PelaajaAPI.git 
```
2. Avaa kopioitu repo koodieditoriin ( . code -komento)
3. Luo virtual enviroment (venv)
    
    a. Visual studio codessa command palette (Ctrl + Shift + P)
    
    b. Python: Create virtual enviroment
    
    c. Vaihtoehdoista _Venv or Conda_, valitse Venv
    
    d. Valitse Python versio ja enter
    
4. tarkista että luomasi venv on myös käynnissä. Jossei käynnisty automaattisesti, syötä alla oleva rimpsu terminaaliin projekti kansiossa:
```
.venv/Scripts/Activate.ps1
```

5. Asenna FastAPI:
```
pip install fastapi uvicorn
```
6. Asenna Sqlalchemy: 
```
pip install sqlalchemy
```
7. Käynnistä
```
uvicorn app.main:app --reload
```
8. Klikkaa linkkiä ja lisää _/docs_ jolloin dokumentaatio aukeaa 

