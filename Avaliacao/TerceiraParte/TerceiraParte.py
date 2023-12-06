from abc import ABC, abstractmethod

class Data:
    def __init__(self, dia=1, mes=1, ano=2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 1800 or ano > 2300:
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
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{:02d}/{:02d}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return self.__dia == outraData.__dia and \
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
    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

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

    @abstractmethod
    def iterador_zip(self, outraLista):
        pass

    @abstractmethod
    def iterador_map(self):
        pass

    @abstractmethod
    def iterador_filter(self):
        pass

    @abstractmethod
    def incluirElemento(self):
        pass

    @abstractmethod
    def listarElementos(self):
        pass

    @abstractmethod
    def reajustarSalarios(self):
        pass

    @abstractmethod
    def modificarDatas(self):
        pass

class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(str)
        self.__lista = []

    def entradaDeDados(self):
        nome = input("Digite um nome: ")
        self.__lista.append(nome)
        print("Nome incluído com sucesso!")

    def mostraMediana(self):
        pass

    def mostraMenor(self):
        pass

    def mostraMaior(self):
        pass

    def listarEmOrdem(self):
        print("Lista de Nomes em Ordem:", sorted(self.__lista))

    def iterador_zip(self, outraLista):
        for nome, salario in zip(self.__lista, outraLista):
            print(f"Nome: {nome}, Salário: {salario}")

    def iterador_map(self):
        pass

    def iterador_filter(self):
        pass

    def incluirElemento(self):
        self.entradaDeDados()

    def listarElementos(self):
        self.listarEmOrdem()

    def reajustarSalarios(self):
        pass

    def modificarDatas(self):
        pass

class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []

    def entradaDeDados(self):
        dia = int(input("Digite o dia: "))
        mes = int(input("Digite o mês: "))
        ano = int(input("Digite o ano: "))
        data = Data(dia, mes, ano)
        self.__lista.append(data)
        print("Data incluída com sucesso!")

    def mostraMediana(self):
        sorted_lista = sorted(self.__lista)
        mid = len(sorted_lista) // 2
        print("Mediana:", sorted_lista[mid])

    def mostraMenor(self):
        print("Menor:", min(self.__lista))

    def mostraMaior(self):
        print("Maior:", max(self.__lista))

    def listarEmOrdem(self):
        sorted_lista = sorted(self.__lista, key=lambda x: (x.ano, x.mes, x.dia))
        print("Lista de Datas em Ordem:")
        for data in sorted_lista:
            print(data)

    def iterador_zip(self, outraLista):
        pass

    def iterador_map(self):
        pass

    def iterador_filter(self):
        pass

    def incluirElemento(self):
        self.entradaDeDados()

    def listarElementos(self):
        self.listarEmOrdem()

    def reajustarSalarios(self):
        pass

    def modificarDatas(self):
        pass

class ListaSalarios(AnaliseDados):
    def __init__(self):
        super().__init__(float)
        self.__lista = []

    def entradaDeDados(self):
        salario = float(input("Digite um salário: "))
        self.__lista.append(salario)
        print("Salário incluído com sucesso!")

    def mostraMediana(self):
        pass

    def mostraMenor(self):
        pass

    def mostraMaior(self):
        pass

    def listarEmOrdem(self):
        print("Lista de Salários em Ordem:", sorted(self.__lista))

    def iterador_zip(self, outraLista):
        pass

    def iterador_map(self):
        pass

    def iterador_filter(self):
        pass

    def incluirElemento(self):
        self.entradaDeDados()

    def listarElementos(self):
        self.listarEmOrdem()

    def reajustarSalarios(self):
        pass

    def modificarDatas(self):
        pass

class ListaIdades(AnaliseDados):
    def __init__(self):
        super().__init__(int)
        self.__lista = []

    def entradaDeDados(self):
        idade = int(input("Digite uma idade: "))
        self.__lista.append(idade)
        print("Idade incluída com sucesso!")

    def mostraMediana(self):
        pass

    def mostraMenor(self):
        pass

    def mostraMaior(self):
        pass

    def listarEmOrdem(self):
        print("Lista de Idades em Ordem:", sorted(self.__lista))

    def iterador_zip(self, outraLista):
        pass

    def iterador_map(self):
        pass

    def iterador_filter(self):
        pass

    def incluirElemento(self):
        self.entradaDeDados()

    def listarElementos(self):
        self.listarEmOrdem()

    def reajustarSalarios(self):
        pass

    def modificarDatas(self):
        pass

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    while True:
        print("\nMenu de Opções:")
        print("1. Incluir um nome na lista de nomes")
        print("2. Incluir uma data na lista de datas")
        print("3. Incluir um salário na lista de salários")
        print("4. Incluir uma idade na lista de idades")
        print("5. Listar elementos")
        print("6. Reajustar salários em 10%")
        print("7. Modificar datas anteriores a 2019")
        print("8. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            nomes.incluirElemento()
        elif opcao == 2:
            datas.incluirElemento()
        elif opcao == 3:
            salarios.incluirElemento()
        elif opcao == 4:
            idades.incluirElemento()
        elif opcao == 5:
            for lista in listaListas:
                lista.listarElementos()
        elif opcao == 6:
            salarios.reajustarSalarios()
        elif opcao == 7:
            datas.modificarDatas()
        elif opcao == 8:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
