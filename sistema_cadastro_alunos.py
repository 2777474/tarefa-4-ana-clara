# Tarefa 02 - Sistema de Cadastro de Alunos
# Disciplina: Introdução à Ciência da Computação
# Aluno(s): Nome 1 (matrícula), Nome 2 (matrícula)
# Data: 17/11/2026

from datetime import datetime


def validar_data_nascimento(data):
    """Valida uma data no formato dd/mm/aaaa."""
    try:
        datetime.strptime(data, "%d/%m/%Y")
    except ValueError as erro:
        raise ValueError("Data inválida. Informe uma data existente no formato dd/mm/aaaa.") from erro


def validar_campos(aluno):
    campos = ("matricula", "nome", "endereco", "data_nasc")
    for campo in campos:
        if not aluno[campo].strip():
            raise ValueError("Todos os campos são obrigatórios.")
    validar_data_nascimento(aluno["data_nasc"])


def cadastrar_aluno(alunos, aluno):
    aluno = {campo: valor.strip() for campo, valor in aluno.items()}
    validar_campos(aluno)
    if aluno["matricula"] in alunos:
        raise ValueError("Já existe um aluno com essa matrícula.")
    alunos[aluno["matricula"]] = aluno


def buscar_alunos(alunos, consulta):
    consulta = consulta.strip().casefold()
    if not consulta:
        return []
    return [
        aluno
        for matricula, aluno in alunos.items()
        if consulta == matricula.casefold()
        or consulta in aluno["nome"].casefold()
    ]


def alterar_aluno(alunos, matricula_atual, novos_dados):
    if matricula_atual not in alunos:
        raise ValueError("Aluno não encontrado.")

    aluno_atualizado = alunos[matricula_atual].copy()
    for campo, valor in novos_dados.items():
        if valor.strip():
            aluno_atualizado[campo] = valor.strip()

    validar_campos(aluno_atualizado)
    nova_matricula = aluno_atualizado["matricula"]
    if nova_matricula != matricula_atual and nova_matricula in alunos:
        raise ValueError("Já existe um aluno com essa matrícula.")

    del alunos[matricula_atual]
    alunos[nova_matricula] = aluno_atualizado


def excluir_aluno(alunos, matricula):
    if matricula not in alunos:
        raise ValueError("Aluno não encontrado.")
    del alunos[matricula]


def exibir_aluno(aluno):
    print(f"Matrícula: {aluno['matricula']}")
    print(f"Nome: {aluno['nome']}")
    print(f"Endereço: {aluno['endereco']}")
    print(f"Data de Nascimento: {aluno['data_nasc']}")
    print("-" * 35)


def ler_dados_aluno():
    return {
        "matricula": input("Matrícula: ").strip(),
        "nome": input("Nome: ").strip(),
        "endereco": input("Endereço: ").strip(),
        "data_nasc": input("Data de Nascimento (dd/mm/aaaa): ").strip(),
    }


def cadastrar_menu(alunos):
    print("\n=== Cadastrar Aluno ===")
    try:
        cadastrar_aluno(alunos, ler_dados_aluno())
        print("Aluno cadastrado com sucesso!")
    except ValueError as erro:
        print(f"Erro: {erro}")


def listar_menu(alunos):
    print("\n=== Alunos Cadastrados ===")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for aluno in alunos.values():
        exibir_aluno(aluno)


def buscar_menu(alunos):
    print("\n=== Buscar Aluno ===")
    consulta = input("Digite o nome ou a matrícula: ")
    resultados = buscar_alunos(alunos, consulta)
    if not resultados:
        print("Nenhum aluno encontrado.")
        return
    for aluno in resultados:
        exibir_aluno(aluno)


def selecionar_aluno(alunos, acao):
    matricula = input(f"Digite a matrícula do aluno que deseja {acao}: ").strip()
    if matricula not in alunos:
        print("Aluno não encontrado.")
        return None
    return matricula


def alterar_menu(alunos):
    print("\n=== Alterar Aluno ===")
    matricula = selecionar_aluno(alunos, "alterar")
    if matricula is None:
        return

    exibir_aluno(alunos[matricula])
    print("Pressione Enter para manter o valor atual.")
    novos_dados = {
        "matricula": input(f"Nova matrícula [{matricula}]: "),
        "nome": input(f"Novo nome [{alunos[matricula]['nome']}]: "),
        "endereco": input(f"Novo endereço [{alunos[matricula]['endereco']}]: "),
        "data_nasc": input(f"Nova data de nascimento [{alunos[matricula]['data_nasc']}]: "),
    }
    try:
        alterar_aluno(alunos, matricula, novos_dados)
        print("Dados do aluno alterados com sucesso!")
    except ValueError as erro:
        print(f"Erro: {erro}")


def excluir_menu(alunos):
    print("\n=== Excluir Aluno ===")
    matricula = selecionar_aluno(alunos, "excluir")
    if matricula is None:
        return

    exibir_aluno(alunos[matricula])
    confirmacao = input("Confirma a exclusão? (s/n): ").strip().casefold()
    if confirmacao != "s":
        print("Exclusão cancelada.")
        return

    excluir_aluno(alunos, matricula)
    print("Aluno excluído com sucesso.")


def main():
    alunos = {}
    while True:
        print("\n=== Sistema de Cadastro de Alunos ===")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Alterar")
        print("5 - Excluir")
        print("0 - Sair")

        opcao = input("Digite a opção: ").strip()
        if opcao == "1":
            cadastrar_menu(alunos)
        elif opcao == "2":
            listar_menu(alunos)
        elif opcao == "3":
            buscar_menu(alunos)
        elif opcao == "4":
            alterar_menu(alunos)
        elif opcao == "5":
            excluir_menu(alunos)
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Escolha uma opção de 0 a 5.")


if __name__ == "__main__":
    main()
