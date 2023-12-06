from abc import ABC, abstractmethod
from typing import List

class Data:
    def __init__(self, dia=1, mes=1, ano=1900):
        self.__validar_data(dia, mes, ano)
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def __validar_data(self, dia, mes, ano):
        if not (1 <= dia <= 31) or not (1 <= mes <= 12) or not (1900 <= ano <= 2100):
            raise ValueError("Data inválida")

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        self.__validar_data(dia, self.__mes, self.__ano)
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        self.__validar_data(self.__dia, mes, self.__ano)
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        self.__validar_data(self.__dia, self.__mes, ano)
        self.__ano = ano
    
    def __str__(self):
        return "{:02d}/{:02d}/{:04d}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outra_data):
        return (self.__dia, self.__mes, self.__ano) == (outra_data.__dia, outra_data.__mes, outra_data.__ano)

    def __lt__(self, outra_data):
        return (self.__ano, self.__mes, self.__dia) < (outra_data.__ano, outra_data.__mes, outra_data.__dia)

    def __gt__(self, outra_data):
        return (self.__ano, self.__mes, self.__dia) > (outra_data.__ano, outra_data.__mes, outra_data.__dia)

    def to_numerical(self):
        return self.__ano * 10000 + self.__mes * 100 + self.__dia

    def __repr__(self):
        return self.__str__()

class AnaliseDados(ABC):
    def __init__(self, tipo_de_dados):
        self._tipo_de_dados = tipo_de_dados
        self._dados = []

    @abstractmethod
    def entrada_de_dados(self):
        pass

    @abstractmethod
    def mostrar_mediana(self):
        pass

    @abstractmethod
    def mostrar_menor(self):
        pass

    @abstractmethod
    def mostrar_maior(self):
        pass

    @abstractmethod
    def listar_em_ordem(self):
        pass

    def calcular_mediana(self):
        dados_ordenados = sorted(self._dados, key=lambda x: x.to_numerical() if isinstance(x, Data) else x)
        tamanho = len(dados_ordenados)

        if tamanho % 2 == 0:
            meio1 = dados_ordenados[tamanho // 2 - 1]
            meio2 = dados_ordenados[tamanho // 2]
            return (meio1.to_numerical() + meio2.to_numerical()) / 2 if isinstance(meio1, Data) else (meio1 + meio2) / 2
        else:
            return dados_ordenados[tamanho // 2].to_numerical() if isinstance(dados_ordenados[tamanho // 2], Data) else dados_ordenados[tamanho // 2]

class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(str)
        self._dados_salarios = []

    def entrada_de_dados(self):
        num_elementos = int(input("\nQuantos nomes deseja inserir na lista? "))
        print("___________________")
        for _ in range(num_elementos):
            nome = input("Digite um nome: ")
            salario = float(input("Digite o salário correspondente: "))
            self._AnaliseDados__dados.append(nome)
            self._dados_salarios.append(salario)

    def mostrar_mediana(self):
        return self.calcular_mediana()

    def mostrar_menor(self):
        return min(self._AnaliseDados__dados)

    def mostrar_maior(self):
        return max(self._AnaliseDados__dados)

    def listar_em_ordem(self):
        return sorted(self._AnaliseDados__dados, key=lambda x: len(x))

    def to_numerical(self, nome):
        return len(nome)

    def iterar_nomes_salarios(self):
        for nome, salario in zip(self._AnaliseDados__dados, self._dados_salarios):
            print(f"Nome: {nome}, Salário: {salario}")

class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(Data)

    def entrada_de_dados(self):
        num_elementos = int(input("Quantas datas deseja inserir na lista? "))
        for _ in range(num_elementos):
            try:
                dia = int(input("Digite o dia: "))
                mes = int(input("Digite o mês: "))
                ano = int(input("Digite o ano: "))
                print("___________________")
                data = Data(dia, mes, ano)
                self._AnaliseDados__dados.append(data)
            except ValueError as e:
                print(f"Erro: {e}. Por favor, insira uma data válida.")

    def mostrar_mediana(self):
        datas_ordenadas = sorted(self._AnaliseDados__dados, key=lambda x: x.to_numerical())
        return self.calcular_mediana()

    def mostrar_menor(self):
        return min(self._AnaliseDados__dados)

    def mostrar_maior(self):
        return max(self._AnaliseDados__dados)

    def listar_em_ordem(self):
        return sorted(self._AnaliseDados__dados, key=lambda x: x.to_numerical())

    def ajustar_datas(self):
        self._AnaliseDados__dados = [Data(1, data.mes, data.ano) if data.ano < 2019 else data for data in self._AnaliseDados__dados]

class ListaSalarios(AnaliseDados):
    def __init__(self):
        super().__init__(float)

    def entrada_de_dados(self):
        num_elementos = int(input("Quantos salários deseja inserir na lista? "))
        for _ in range(num_elementos):
            salario = float(input("Digite um salário: "))
            self._AnaliseDados__dados.append(salario)

    def mostrar_mediana(self):
        return self.calcular_mediana()

    def mostrar_menor(self):
        return min(self._AnaliseDados__dados)

    def mostrar_maior(self):
        return max(self._AnaliseDados__dados)

    def listar_em_ordem(self):
        return sorted(self._AnaliseDados__dados)

    def reajustar_salarios(self, percentual):
        self._AnaliseDados__dados = list(map(lambda x: x * (1 + percentual / 100), self._AnaliseDados__dados))

class ListaIdades(AnaliseDados):
    def __init__(self):
        super().__init__(int)

    def entrada_de_dados(self):
        num_elementos = int(input("Quantas idades deseja inserir na lista? "))
        for _ in range(num_elementos):
            idade = int(input("Digite uma idade: "))
            self._AnaliseDados__dados.append(idade)

    def mostrar_mediana(self):
        return self.calcular_mediana()

    def mostrar_menor(self):
        return min(self._AnaliseDados__dados)

    def mostrar_maior(self):
        return max(self._AnaliseDados__dados)

    def listar_em_ordem(self):
        return sorted(self._AnaliseDados__dados)

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listas = [nomes, datas, salarios, idades]

    for lista in listas:
        lista.entrada_de_dados()
        print("Mediana:", lista.mostrar_mediana())
        print("Menor:", lista.mostrar_menor())
        print("Maior:", lista.mostrar_maior())
        print("Em ordem:", lista.listar_em_ordem())
        print("___________________")

    nomes.iterar_nomes_salarios()
    print("___________________")

    salarios.reajustar_salarios(10)
    print("Salários reajustados:", salarios.listar_em_ordem())
    print("___________________")

    datas.ajustar_datas()
    print("Datas ajustadas:", datas.listar_em_ordem())
    print("___________________")

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
