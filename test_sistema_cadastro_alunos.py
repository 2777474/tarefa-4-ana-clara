import unittest

from sistema_cadastro_alunos import (
    alterar_aluno,
    buscar_alunos,
    cadastrar_aluno,
    excluir_aluno,
)


class SistemaCadastroAlunosTest(unittest.TestCase):
    def setUp(self):
        self.alunos = {}
        self.aluno = {
            "matricula": "25100003",
            "nome": "Pedro Oliveira",
            "endereco": "Rua XV de Novembro, 100",
            "data_nasc": "10/05/2006",
        }

    def test_cadastrar_e_impedir_matricula_duplicada(self):
        cadastrar_aluno(self.alunos, self.aluno)
        with self.assertRaisesRegex(ValueError, "Já existe"):
            cadastrar_aluno(self.alunos, self.aluno)
        self.assertEqual(len(self.alunos), 1)

    def test_validar_campos_obrigatorios_e_data(self):
        aluno_incompleto = dict(self.aluno, nome=" ")
        with self.assertRaisesRegex(ValueError, "obrigatórios"):
            cadastrar_aluno(self.alunos, aluno_incompleto)

        aluno_data_invalida = dict(self.aluno, data_nasc="31/02/2006")
        with self.assertRaisesRegex(ValueError, "Data inválida"):
            cadastrar_aluno(self.alunos, aluno_data_invalida)

    def test_buscar_por_nome_ou_matricula(self):
        cadastrar_aluno(self.alunos, self.aluno)
        self.assertEqual(buscar_alunos(self.alunos, "pedro"), [self.aluno])
        self.assertEqual(buscar_alunos(self.alunos, "25100003"), [self.aluno])
        self.assertEqual(buscar_alunos(self.alunos, "ausente"), [])

    def test_alterar_dados_e_matricula(self):
        cadastrar_aluno(self.alunos, self.aluno)
        alterar_aluno(
            self.alunos,
            "25100003",
            {"matricula": "25100004", "nome": "Pedro Silva"},
        )
        self.assertNotIn("25100003", self.alunos)
        self.assertEqual(self.alunos["25100004"]["nome"], "Pedro Silva")

    def test_excluir_aluno(self):
        cadastrar_aluno(self.alunos, self.aluno)
        excluir_aluno(self.alunos, "25100003")
        self.assertEqual(self.alunos, {})


if __name__ == "__main__":
    unittest.main()
