SELECT * 
FROM dane_zagregowane a Join stanowiska_pomiarowe b on a.stacja = b.kod_stacja
WHERE a.stacja = '01ZM'