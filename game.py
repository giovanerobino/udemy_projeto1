"""
Parte principal do jogo, onde começa jogar só com um número ramdômico com 3 dificuldades
"""
import colorama
from colorama import Fore
from models.calcular import Calcular

# inicializa o colorama
colorama.init(autoreset = True)

# vamos inicializar pontos com zero e vai executar a função jogar(), passando os pts.
def main() -> None:
    """inicializa o jogo com zero pontos"""
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    """recebe pontos e pergunta a dificuldade pra iniciar o jogo"""
    try:
        dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3, ou 4]: '))

        if dificuldade not in [1, 2, 3, 4]:
            print('Nivel de dificuldade invalido. Tente novamente')
            return jogar(pontos)
        # estancia a classe e passa a dificuldade
        calc: Calcular = Calcular(dificuldade)
        print('Informe o resultado para a seguinte operação: ')
        # mostra a operação
        calc.mostrar_operacao()
        # pede a resposta
        resultado: int = int(input())
        # pega o objeto e checa a resposta com o resultado
        if calc.checar_resultado(resultado):
            pontos += 1  # se for True soma mais um aos pontos
            # informa os pontos
            print(f'Você tem {pontos} pontos.')
        # pergunta se deseja jogar novamente (precisa tratar o erro se nao digar 1 ou 2)
        continuar: int = int(input('Jogar novamente? \n[' + Fore.GREEN + '1 - Sim' + Fore.WHITE + ' | ' + Fore.RED + '0 - Nao' + Fore.WHITE + '] \n'))

        if continuar:
            jogar(pontos)  # se ele quiser continuar executa a função jogar() novamente
        else:
            # se ele não quiser continuar, mostra os pontos que ele fez e finaliza o jogo
            print(Fore.GREEN + 'Voce termina o jogo com ' + Fore.BLUE + (str(pontos)) + Fore.GREEN + ' pontos.')
            print('Parabens! Fim do jogo!')
    except ValueError:
        print('Dificuldade invalida. Tente novamente')
        return jogar(pontos)



# quando executar-mos o game python game.py vai iniciar o main()
if __name__ == '__main__':
    main()
