#Esercizio 3C-5

utente = {}

utente["Nome"]=(input("Digitare nome dell'utente "))

utente["Ruolo"]=(input("Digitare ruolo dell'utente "))

utente["Età"]=int(input("Digitare l'età dell'utente "))

match utente:
    case {"Ruolo": "Admin"}:
        print("Accesso completo a tutte le funzionalità")
    case {"Ruolo": "Moderatore"}:
        print("Può gestire i contenuti ma non modificare le impostazioni")
    case utente if utente["Età"] >= 18 and utente["Ruolo"]== utente:
        print("Accesso standard a tutti i servizi")
    case utente if utente ["Età"] < 18 and utente["Ruolo"]== utente:
        print("Accesso limitato! Alcune funzionalità sono bloccate")
    case {"Ruolo": "Ospite"}:
        print("Accesso ristretto! Solo visualizzazione dei contenuti")
    case _:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")