"""
Este modulo contem a classe Calcular, que eh usada para realizar as operacoes matematicas.
"""
from random import randint
import colorama
from colorama import Fore


# inicializa o colorama
colorama.init(autoreset = True)

class Calcular:
    """Classe para realizar as operações matematicas"""

    def __init__(self: object, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        # 1 = somar, 2 = subtrair, 3 = multiplicar
        self.__operacao: int = randint(1, 3)
        self.__resultado: int = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        """gera a dificuldade"""
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        """gera o valor 1"""
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        """gera o valor 2"""
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        """gera a operação"""
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        """gera o resultado da operação"""
        return self.__resultado

    def __str__(self: object) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Subtrair'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação inválida'
        return (f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \n'
                f'Dificuldade: {self.dificuldade} \nOperação: {op}')

    @property
    def _gerar_valor(self: object) -> int:

        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    @property
    def _gerar_resultado(self: object) -> int:

        if self.operacao == 1:  # somar
            return self.valor1 + self.valor2
        elif self.operacao == 2:  # subtrair
            if self.valor1 < self.valor2:
                return self.valor2 - self.valor1
            else:
                return self.valor1 - self.valor2
        else:  # multiplicar
            return self.valor1 * self.valor2

    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        else:
            return '*'

    def checar_resultado(self: object, resposta: int) -> bool:
        """recebe a resposta do jogador e compara com o resultado do objeto"""
        certo: bool = False
        # se a resposta do jogador for igual a do objeto retorna True
        if self.resultado == resposta:
            print(Fore.GREEN + 'Resposta correta!')
            certo = True
        else:
            print(Fore.RED + 'Resposta errada!')  # se errar a resposta, mostra essa msg
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo

    def mostrar_operacao(self: object) -> None:
        """mostra a operação para o jogador"""
        if self.valor1 < self.valor2 and self._op_simbolo == '-':
            print(f'{self.valor2} {self._op_simbolo} {self.valor1} = ?')
        else:
            print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')
