# PROJETO 1 – To-Do List no terminal (com salvamento em JSON)
"""
    Objetivo:
    Permitir que o usuário adicione, liste e remova tarefas diretamente pelo terminal. 
    As tarefas são salvas em um arquivo .json.
"""

import json
import os

ARQUIVOS_TAREFAS = 'tarefas.json'

def carregar_tarefas():
    if os.path.exists(ARQUIVOS_TAREFAS):
        with open(ARQUIVOS_TAREFAS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVOS_TAREFAS, 'w', encoding='utf-8') as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\nTarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a nova tarefa: ").strip()
    if tarefa:
        tarefas.append(tarefa)
        salvar_tarefas(tarefas)
        print("Tarefa adicionada.")
    else:
         print("Tarefa vazia! Não foi adicionada.")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        num = int(input("Digite o número da tarefa para remover: "))
        if 1 <= num <= len(tarefas):
            removida = tarefas.pop(num - 1)
            salvar_tarefas(tarefas)
            print(f"Tarefa '{removida}' removida.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    tarefas = carregar_tarefas()
    while True:
        print("\n--- MENU ---")
        print("1. Listar tarefas")
        print("2. Adiciona tarefas")
        print("3. Remover tarefa")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            listar_tarefas(tarefas)
        elif escolha == '2':
            adicionar_tarefa(tarefas)
        elif escolha == '3':
            remover_tarefa(tarefas)
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida")

if __name__ == '__main__':
    menu()