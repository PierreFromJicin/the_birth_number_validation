# Zadání domácího úkolu do příští soboty tj. 15.09.2022:

napište funkci validující rodné číslo, funkce bere jako parameter string s rodným číslem a vrátí True nebo False v
závislosti na výsledku validace. K funkci přidejte pozitivní a negativní Pytest test case.

Zkuste použit programování s cyklem.

### Něco málo o RČ:

Rodné číslo je desetimístné číslo, které je dělitelné jedenácti beze zbytku. První dvojčíslí vyjadřuje poslední dvě
číslice roku narození, druhé dvojčíslí vyjadřuje měsíc narození, u žen zvýšené o 50, třetí dvojčíslí vyjadřuje den
narození. Čtyřmístná koncovka je rozlišujícím znakem fyzických osob narozených v tomtéž kalendářním dnu o rozsahu
přidělovaných koncovek 0000 až 9999 (Pozn.: Rodná čísla se čtyřmístnou nulovou koncovkou, odpovídají-li definici rodného
čísla, mohou být rodným číslem přiděleným konkrétní fyzické osobě, neboť tato rodná čísla byla v minulosti přidělována.
Nicméně od přidělování rodných čísel se čtyřmístnou nulovou koncovkou bylo v minulosti upuštěno.).

Rodná čísla přidělená fyzickým osobám narozeným před 1. 1. 1954 mají stejnou strukturu, jsou však devítimístná s
třímístnou koncovkou a nesplňují podmínku dělitelnosti jedenácti; rodné číslo s třímístnou nulovou koncovkou není rodným
číslem, neboť pro každý kalendářní den v roce byla generována rodná čísla s třímístnou koncovkou pouze v rozsahu 001 až
999.

zdroj: [MVČR](https://www.mvcr.cz/clanek/rady-a-sluzby-dokumenty-rodne-cislo.aspx "odkaz na website")
