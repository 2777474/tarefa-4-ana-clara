# Tarefa 02 - Sistema de Cadastro de Alunos

Programa de terminal para cadastrar e gerenciar alunos. Os dados ficam em
memória enquanto o programa está em execução e não são gravados em arquivos.

## Funcionalidades

- Cadastrar, listar, buscar, alterar e excluir alunos.
- Buscar por matrícula ou por parte do nome.
- Validar campos obrigatórios, datas e matrículas únicas.
- Confirmar a exclusão antes de remover um cadastro.

## Requisitos

- Python 3.8 ou superior.

## Executar

```powershell
py -3 sistema_cadastro_alunos.py
```

## Testes

Execute a partir da pasta que contém este README:

```powershell
py -3 -m unittest -v test_sistema_cadastro_alunos.py
```

Antes de entregar, substitua `Nome 1 (matrícula), Nome 2 (matrícula)` no
cabeçalho do arquivo Python pelos nomes e matrículas corretos dos alunos.
