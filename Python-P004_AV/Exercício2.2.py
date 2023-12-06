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
        return "{:02d}/{:02d}/{:04d}".format(self.__dia, self.__mes, self.__ano)

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

    def to_numerical(self):
        return self.__ano * 10000 + self.__mes * 100 + self.__dia
    
    def __repr__(self):
        return self.__str__()

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
        lista_ordenada = sorted(self.__dados, key=lambda x: x.to_numerical() if isinstance(x, Data) else x)
        tamanho = len(lista_ordenada)

        if tamanho % 2 == 0:
            meio1 = lista_ordenada[tamanho // 2 - 1]
            meio2 = lista_ordenada[tamanho // 2]
            return (meio1.to_numerical() + meio2.to_numerical()) / 2 if isinstance(meio1, Data) else (meio1 + meio2) / 2
        else:
            return lista_ordenada[tamanho // 2].to_numerical() if isinstance(lista_ordenada[tamanho // 2], Data) else lista_ordenada[tamanho // 2]

class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(str)
        self.__dados_salarios = []

    def entradaDeDados(self):
        num_elementos = int(input("\nQuantos nomes deseja inserir na lista? "))
        print("___________________")
        for _ in range(num_elementos):
            nome = input("Digite um nome: ")
            salario = float(input("Digite o salário correspondente: "))
            self._AnaliseDados__dados.append(nome)
            self.__dados_salarios.append(salario)

    def mostraMediana(self):
        return self.calcularMediana()

    def mostraMenor(self):
        return min(self._AnaliseDados__dados)

    def mostraMaior(self):
        return max(self._AnaliseDados__dados)

    def listarEmOrdem(self):
        return sorted(self._AnaliseDados__dados, key=lambda x: len(x))

    def to_numerical(self, nome):
        return len(nome)

    def iterarNomesSalarios(self):
        for nome, salario in zip(self._AnaliseDados__dados, self.__dados_salarios):
            print(f"Nome: {nome}, Salário: {salario}")

class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(Data)

    def entradaDeDados(self):
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

    def mostraMediana(self):
        datas_ordenadas = sorted(self._AnaliseDados__dados, key=lambda x: x.to_numerical())
        return self.calcularMediana()

    def mostraMenor(self):
        return min(self._AnaliseDados__dados)

    def mostraMaior(self):
        return max(self._AnaliseDados__dados)

    def listarEmOrdem(self):
        return sorted(self._AnaliseDados__dados, key=lambda x: x.to_numerical())

    def ajustarDatas(self):
        self._AnaliseDados__dados = [Data(1, data.mes, data.ano) if data.ano < 2019 else data for data in self._AnaliseDados__dados]

class ListaSalarios(AnaliseDados):
    def __init__(self):
        super().__init__(float)

    def entradaDeDados(self):
        num_elementos = int(input("Quantos salários deseja inserir na lista? "))
        for _ in range(num_elementos):
            salario = float(input("Digite um salário: "))
            self._AnaliseDados__dados.append(salario)

    def mostraMediana(self):
        return self.calcularMediana()

    def mostraMenor(self):
        return min(self._AnaliseDados__dados)

    def mostraMaior(self):
        return max(self._AnaliseDados__dados)

    def listarEmOrdem(self):
        return sorted(self._AnaliseDados__dados)

    def reajustarSalarios(self, percentual):
        self._AnaliseDados__dados = list(map(lambda x: x * (1 + percentual / 100), self._AnaliseDados__dados))

class ListaIdades(AnaliseDados):
    def __init__(self):
        super().__init__(int)

    def entradaDeDados(self):
        num_elementos = int(input("Quantas idades deseja inserir na lista? "))
        for _ in range(num_elementos):
            idade = int(input("Digite uma idade: "))
            self._AnaliseDados__dados.append(idade)

    def mostraMediana(self):
        return self.calcularMediana()

    def mostraMenor(self):
        return min(self._AnaliseDados__dados)

    def mostraMaior(self):
        return max(self._AnaliseDados__dados)

    def listarEmOrdem(self):
        return sorted(self._AnaliseDados__dados)

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        print("Mediana:", lista.mostraMediana())
        print("Menor:", lista.mostraMenor())
        print("Maior:", lista.mostraMaior())
        print("Em ordem:", lista.listarEmOrdem())
        print("___________________")

    nomes.iterarNomesSalarios()
    print("___________________")

    salarios.reajustarSalarios(10)
    print("Salários reajustados:", salarios.listarEmOrdem())
    print("___________________")

    datas.ajustarDatas()
    print("Datas ajustadas:", datas.listarEmOrdem())
    print("___________________")

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
