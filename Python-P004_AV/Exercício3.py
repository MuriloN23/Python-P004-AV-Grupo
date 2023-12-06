from abc import ABC, abstractmethod
from typing import List

class Data:
    def __init__(self, dia=1, mes=1, ano=1900):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 1900 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 1900 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False

class AnaliseDados(ABC):
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados
        self.__dados = []

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass

    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

    @abstractmethod
    def listarEmOrdem(self):
        pass

    def calcularMediana(self):
        lista_ordenada = sorted(self.__dados)
        tamanho = len(lista_ordenada)

        if tamanho % 2 == 0:
            meio1 = lista_ordenada[tamanho // 2 - 1]
            meio2 = lista_ordenada[tamanho // 2]
            return (meio1 + meio2) / 2
        else:
            return lista_ordenada[tamanho // 2]

    def menu_opcoes(self):
        while True:
            print("\nMenu de Opções:")
            print("1. Incluir dado")
            print("2. Mostrar Mediana")
            print("3. Mostrar Menor")
            print("4. Mostrar Maior")
            print("5. Listar em Ordem")
            print("6. Sair")

            escolha = int(input("Escolha uma opção: "))

            if escolha == 1:
                self.entradaDeDados()
            elif escolha == 2:
                print("Mediana:", self.mostraMediana())
            elif escolha == 3:
                print("Menor:", self.mostraMenor())
            elif escolha == 4:
                print("Maior:", self.mostraMaior())
            elif escolha == 5:
                print("Listar em Ordem:")
                self.listarEmOrdem()
            elif escolha == 6:
                break
            else:
                print("Opção inválida. Tente novamente.")

    @abstractmethod
    def incluir_nome(self):
        pass

    @abstractmethod
    def incluir_salario(self):
        pass

    @abstractmethod
    def incluir_data(self):
        pass

    @abstractmethod
    def incluir_idade(self):
        pass

    @abstractmethod
    def percorrer_listas(self):
        pass

    @abstractmethod
    def reajustar_salarios(self):
        pass

    @abstractmethod
    def modificar_datas(self):
        pass

    @abstractmethod
    def listarEmOrdem(self):
        pass

class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(str)

    def entradaDeDados(self):
        nome = input("Digite um nome: ")
        self.__dados.append(nome)

    def mostraMediana(self):
        return self.calcularMediana()

    def mostraMenor(self):
        return min(self.__dados)

    def mostraMaior(self):
        return max(self.__dados)

    def listarEmOrdem(self):
        print(sorted(self.__dados))

    def incluir_nome(self):
        nome = input("Digite um nome: ")
        self.__dados.append(nome)

    def incluir_salario(self):
        print("Operação não permitida nesta lista.")

    def incluir_data(self):
        print("Operação não permitida nesta lista.")

    def incluir_idade(self):
        print("Operação não permitida nesta lista.")

    def percorrer_listas(self):
        for nome in self.__dados:
            print(f"Nome: {nome}")

    def reajustar_salarios(self):
        print("Operação não permitida nesta lista.")

    def modificar_datas(self):
        print("Operação não permitida nesta lista.")

class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(Data)

    def entradaDeDados(self):
        try:
            dia = int(input("Digite o dia: "))
            mes = int(input("Digite o mês: "))
            ano = int(input("Digite o ano: "))
            data = Data(dia, mes, ano)
            self.__dados.append(data)
        except ValueError as e:
            print(f"Erro: {e}. Por favor, insira uma data válida.")

    def mostraMediana(self):
        datas_ordenadas = sorted(self.__dados, key=lambda x: (x.ano, x.mes, x.dia))
        return self.calcularMediana()

    def mostraMenor(self):
        return min(self.__dados)

    def mostraMaior(self):
        return max(self.__dados)

    def listarEmOrdem(self):
        print(sorted(self.__dados, key=lambda x: (x.ano, x.mes, x.dia)))

    def incluir_nome(self):
        print("Operação não permitida nesta lista.")

    def incluir_salario(self):
        print("Operação não permitida nesta lista.")

    def incluir_data(self):
        try:
            dia = int(input("Digite o dia: "))
            mes = int(input("Digite o mês: "))
            ano = int(input("Digite o ano: "))
            data = Data(dia, mes, ano)
            self.__dados.append(data)
        except ValueError as e:
            print(f"Erro: {e}. Por favor, insira uma data válida.")

    def incluir_idade(self):
        print("Operação não permitida nesta lista.")

    def percorrer_listas(self):
        for data in self.__dados:
            print(f"Data: {data}")

    def reajustar_salarios(self):
        print("Operação não permitida nesta lista.")

    def modificar_datas(self):
        print("Operação não permitida nesta lista.")

class ListaSalarios(AnaliseDados):
    def __init__(self):
        super().__init__(float)

    def entradaDeDados(self):
        salario = float(input("Digite um salário: "))
        self.__dados.append(salario)

    def mostraMediana(self):
        return self.calcularMediana()

    def mostraMenor(self):
        return min(self.__dados)

    def mostraMaior(self):
        return max(self.__dados)

    def listarEmOrdem(self):
        print(sorted(self.__dados))

    def incluir_nome(self):
        print("Operação não permitida nesta lista.")

    def incluir_salario(self):
        salario = float(input("Digite um salário: "))
        self.__dados.append(salario)

    def incluir_data(self):
        print("Operação não permitida nesta lista.")

    def incluir_idade(self):
        print("Operação não permitida nesta lista.")

    def percorrer_listas(self):
        for salario in self.__dados:
            print(f"Salário: {salario}")

    def reajustar_salarios(self):
        self.__dados = [salario * 1.1 for salario in self.__dados]

    def modificar_datas(self):
        print("Operação não permitida nesta lista.")

class ListaIdades(AnaliseDados):
    def __init__(self):
        super().__init__(int)

    def entradaDeDados(self):
        idade = int(input("Digite uma idade: "))
        self.__dados.append(idade)

    def mostraMediana(self):
        return self.calcularMediana()

    def mostraMenor(self):
        return min(self.__dados)

    def mostraMaior(self):
        return max(self.__dados)

    def listarEmOrdem(self):
        print(sorted(self.__dados))

    def incluir_nome(self):
        print("Operação não permitida nesta lista.")

    def incluir_salario(self):
        print("Operação não permitida nesta lista.")

    def incluir_data(self):
        print("Operação não permitida nesta lista.")

    def incluir_idade(self):
        idade = int(input("Digite uma idade: "))
        self.__dados.append(idade)

    def percorrer_listas(self):
        for idade in self.__dados:
            print(f"Idade: {idade}")

    def reajustar_salarios(self):
        print("Operação não permitida nesta lista.")

    def modificar_datas(self):
        print("Operação não permitida nesta lista.")

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    while True:
        for i, lista in enumerate(listaListas, start=1):
            print(f"{i}. {lista.__class__.__name__}")

        escolha = int(input("Escolha uma opção (ou 0 para sair): "))

        if escolha == 0:
            break

        lista = listaListas[escolha - 1]
        lista.menu_opcoes()

    print("Fim do programa.")

if __name__ == "__main__":
    main()
