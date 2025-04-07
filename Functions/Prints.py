def print_apartments(apartments:list):
    for apartment in apartments:
        payday = round(apartment.payday)
        rent = f"{round(apartment.rent)},00"
        print(f"Apto. {apartment.apartment_number}|{apartment.condominium} - {apartment.tenant} - Dia de vencimento: {payday} / Valor: R& {rent}")