pc={"Processador":1500,"Placa-mãe":500,"Memória-RAM":600,"Placa-de-Vídeo":1200}
while True:
    componente=input("Digite o nome do componente ou 'fim' para sair:")
    if componente=="fim":
     break
    if componente in pc:
        print(f"Preço{pc[componente]:5.2f}")
    else:
        print("Produto não encontrado")
del pc["Placa-de-Vídeo"]
print(pc)
