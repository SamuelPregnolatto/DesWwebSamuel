largura = float(input("Defina uma largura em metros: "))
comprimento = float(input("Defina um comprimento em metros: "))
lata_tintas = float(input("Digite a quantidade de tinta por lata em litros: "))
pe_direito = 2.80

area_paredes =(largura * pe_direito) + 2 * (comprimento * pe_direito)
largura_porta = 0.80
altura_porta = 2.10
area_porta = largura_porta * altura_porta
area_parede_porta = area_paredes - area_porta

quantidade_litros_necessario = area_paredes / 3 and area_parede_porta / 3
quantidade_latas_necessaria = quantidade_litros_necessario / lata_tintas

print (f"A quantidade de latas de tintas necessárias para pintar as paredes do comodo são {quantidade_latas_necessaria:.2f} latas")



