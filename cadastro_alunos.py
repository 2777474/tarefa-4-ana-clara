# Tarefa 02 - Sistema de Cadastro de Alunos
# Disciplina: Introdução à Ciência da Computação
# Aluno(s): Nome 1 (matrícula), Nome 2 (matrícula)
# Data: 17/11/2026

from datetime import datetime


alunos = {}


def ler_obrigatorio(rotulo):
    while True:
        valor = input(rotulo).strip()
        if valor:
            return valor
        print("Erro: este campo é obrigatório.")


def ler_data_nascimento(rotulo="Data de Nascimento: "):
    while True:
        data = ler_obrigatorio(rotulo)
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            print("Erro: informe uma data válida no formato dd/mm/aaaa.")


def cadastrar_aluno():
    print("\n=== Cadastrar Aluno ===")
    matricula = ler_obrigatorio("Matrícula: ")
    if matricula in alunos:
        print("Erro: já existe um aluno cadastrado com essa matrícula.")
        return

    alunos[matricula] = {
        "nome": ler_obrigatorio("Nome: "),
        "endereco": ler_obrigatorio("Endereço: "),
        "data_nasc": ler_data_nascimento(),
    }
    print("Aluno cadastrado com sucesso!")


def listar_alunos():
    print("\n=== Alunos Cadastrados ===")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for matricula, aluno in alunos.items():
        exibir_aluno(matricula, aluno)


def exibir_aluno(matricula, aluno):
    print(f"\nMatrícula: {matricula}")
    print(f"Nome: {aluno['nome']}")
    print(f"Endereço: {aluno['endereco']}")
    print(f"Data de Nascimento: {aluno['data_nasc']}")


def buscar_aluno():
    print("\n=== Buscar Aluno ===")
    termo = ler_obrigatorio("Digite o nome ou a matrícula: ").casefold()
    encontrados = [
        (matricula, aluno)
        for matricula, aluno in alunos.items()
        if termo in matricula.casefold() or termo in aluno["nome"].casefold()
    ]

    if not encontrados:
        print("Nenhum aluno encontrado.")
        return

    for matricula, aluno in encontrados:
        exibir_aluno(matricula, aluno)


def alterar_aluno():
    print("\n=== Alterar Aluno ===")
    matricula = ler_obrigatorio("Matrícula do aluno: ")
    aluno = alunos.get(matricula)
    if aluno is None:
        print("Erro: não há aluno cadastrado com essa matrícula.")
        return

    exibir_aluno(matricula, aluno)
    print("\nPressione Enter para manter o valor atual.")

    nova_matricula = input(f"Nova matrícula [{matricula}]: ").strip()
    if nova_matricula and nova_matricula != matricula:
        if nova_matricula in alunos:
            print("Erro: já existe um aluno cadastrado com essa matrícula.")
            return
        alunos[nova_matricula] = alunos.pop(matricula)
        matricula = nova_matricula
        aluno = alunos[matricula]

    for campo, rotulo in (
        ("nome", "Nome"),
        ("endereco", "Endereço"),
        ("data_nasc", "Data de Nascimento"),
    ):
        valor_atual = aluno[campo]
        novo_valor = input(f"{rotulo} [{valor_atual}]: ").strip()
        if not novo_valor:
            continue
        if campo == "data_nasc":
            while True:
                try:
                    datetime.strptime(novo_valor, "%d/%m/%Y")
                    break
                except ValueError:
                    print("Erro: informe uma data válida no formato dd/mm/aaaa.")
                    novo_valor = ler_obrigatorio(f"{rotulo}: ")
        aluno[campo] = novo_valor

    print("Dados do aluno alterados com sucesso!")


def excluir_aluno():
    print("\n=== Excluir Aluno ===")
    matricula = ler_obrigatorio("Matrícula do aluno: ")
    aluno = alunos.get(matricula)
    if aluno is None:
        print("Erro: não há aluno cadastrado com essa matrícula.")
        return

    exibir_aluno(matricula, aluno)
    confirmacao = input("Confirma a exclusão? (S/N): ").strip().casefold()
    if confirmacao == "s":
        del alunos[matricula]
        print("Aluno excluído com sucesso.")
    else:
        print("Exclusão cancelada.")


def exibir_menu():
    print("\n=== Sistema de Cadastro de Alunos ===")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar")
    print("4 - Alterar")
    print("5 - Excluir")
    print("0 - Sair")


def main():
    while True:
        exibir_menu()
        opcao = input("Digite a opção: ").strip()

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            buscar_aluno()
        elif opcao == "4":
            alterar_aluno()
        elif opcao == "5":
            excluir_aluno()
        elif opcao == "0":
            print("Sistema encerrado.")
            break
        else:
            print("Erro: opção inválida. Escolha uma opção de 0 a 5.")


if __name__ == "__main__":
    main()
