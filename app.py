from modelo.restaurante import Restaurante
from modelo.cardapio.bebida import Bebida
from modelo.cardapio.prato import Prato
from modelo.cardapio.sobremesa import Sobremesa

restaurante_1 = Restaurante('Lupi', 'Pizza&Vinhos')
suco_limonada = Bebida('Limonada Suíça', 6.00, 'Copo')
suco_limonada.aplicar_desconto()
almoco_executivo = Prato('Arrumadinho', 25.00, 'Feijão verde com arroz, acompanhado de charque desfiada')
almoco_executivo.aplicar_desconto()
restaurante_1.adicionar_no_cardapio(suco_limonada)
restaurante_1.adicionar_no_cardapio(almoco_executivo)



def main():
    restaurante_1.exibir_cardapio
    

if __name__ == '__main__':
    main()