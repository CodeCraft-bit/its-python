
nord_sud:int = int(input("Inserisci la soglia nord_sud: "))
est_ovest:int = int(input("Inserisci la soglia est_ovest: "))
soglia:int = 70

if nord_sud > soglia and est_ovest > soglia:
    time_ns = 50
    time_eo = 50
if nord_sud > soglia:
    time_ns = 60
    time_eo = 40
if est_ovest > soglia:
    time_ns = 40
    time_eo = 60
else:
    time_ns = (nord_sud/(nord_sud + est_ovest)) * 100
    time_eo = (est_ovest/(nord_sud + est_ovest)) * 100
print(f"Il tempo assegnato alla direzione nord_sud è: {time_ns:.2f}")
print(f"Il tempo assegnato alla direzione est_ovest è: {time_eo:.2f}")