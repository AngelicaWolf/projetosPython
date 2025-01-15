pc={"Processador":1500,"Placa-mãe":500,"Memória-RAM":600,"Placa-de-Vídeo":1200}
while True:
    component=input("Digite o nome do componente ou 'fim' para sair:")
    if component=="fim":
     break
    if component in pc:
        print(f"Preço{pc[component]:5.2f}")
    else:
        print("Produto não encontrado")
del pc["Placa-de-Vídeo"]
print(pc)
