import random

def simulace_gce(pocet_kroku, c_max):
    # Na začátku máme dva uzly (ID 0 a 1), které jsou spolu spojené.
    # Slovník 'uzly' si pamatuje, kolik má každý uzel čar (vazeb).
    uzly = {0: 1, 1: 1}  
    dalsi_id = 2
    
    v_in = 1  # Stabilní relace (gravitace/hmota)
    v_out = 0 # Odražené relace (expanze/vakuum)
    
    for krok in range(pocet_kroku):
        # 1. MOTOR: Vybereme dva náhodné existující uzly
        vsechny_id = list(uzly.keys())
        a, b = random.sample(vsechny_id, 2)
        
        # 2. TEST LIMITU: Mají oba uzly ještě volnou kapacitu?
        if uzly[a] < c_max and uzly[b] < c_max:
            # ANO: Relace se uzavřela lokálně
            uzly[a] += 1
            uzly[b] += 1
            v_in += 1
            
        else:
            # NE: Narazili jsme na limit Strukturálního atomu (alespoň jeden je plný)
            # Relace se "odráží" ven a tvoří nový prostor.
            v_out += 1
            
            # Musíme vyrobit nový uzel, ale aby nebyl odtržený od existence (díra v realitě),
            # připojíme ho k nějakému uzlu, který ještě má místo.
            uzly_s_mistem = [u for u, kapacita in uzly.items() if kapacita < c_max]
            
            if uzly_s_mistem:
                # Vybereme náhodný uzel s volným místem
                cil = random.choice(uzly_s_mistem)
                uzly[cil] += 1
                uzly[dalsi_id] = 1 # Nový uzel vzniká s jednou čarou
                dalsi_id += 1
            else:
                # Extrémní případ - celá síť je úplně plná
                break

    return v_in, v_out

# === SPUŠTĚNÍ SIMULACE ===
KROKY = 100000
KAPACITA_UZLU = 4  # Zkusíme nastavit maximální limit na 4 vazby

print("Simuluji vývoj vesmíru podle GCE...")
hmota, vakuum = simulace_gce(KROKY, KAPACITA_UZLU)

celkem = hmota + vakuum
print("\n=== VÝSLEDKY ===")
print(f"Vnitřní vazby (Hmota): {hmota} ({(hmota/celkem)*100:.1f} %)")
print(f"Odražené vazby (Vakuum): {vakuum} ({(vakuum/celkem)*100:.1f} %)")
print(f"\nPOMĚR Vakuum / Hmota: {vakuum / hmota:.2f}")