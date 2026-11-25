#nome: Erick Dos Santos Lima#
import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione ENTER para continuar...")


# Lista de usuarios: cada item eh um dicionario {"nome": ..., "login": ..., "senha": ...}
usuarios = [
    {"nome": "Administrador", "login": "admin", "senha": "admin"}
]


def buscar_usuario_por_login(login):
    for u in usuarios:
        if u["login"] == login:
            return u
    return None


def cadastrar_usuario():
    print("=== CADASTRAR USUARIO ===")
    nome = input("Nome: ").strip()
    if not nome:
        print("Erro: o nome nao pode ficar vazio.")
        return

    login = input("Login: ").strip()
    if not login:
        print("Erro: o login nao pode ficar vazio.")
        return

    if buscar_usuario_por_login(login) is not None:
        print("Erro: ja existe um usuario com esse login.")
        return

    senha = input("Senha (minimo 4 caracteres): ")
    if len(senha) < 4:
        print("Erro: a senha deve ter pelo menos 4 digitos.")
        return

    novo_usuario = {
        "nome": nome,
        "login": login,
        "senha": senha
    }
    usuarios.append(novo_usuario)
    print("Usuario cadastrado com sucesso!")


def pesquisar_usuario():
    print("=== PESQUISAR USUARIO ===")
    login = input("Digite o login para buscar: ").strip()
    usuario = buscar_usuario_por_login(login)

    if usuario is None:
        print("Usuario nao encontrado.")
    else:
        print(f"Login: {usuario['login']} | Nome: {usuario['nome']}")


def remover_usuario():
    print("=== REMOVER USUARIO ===")
    login = input("Digite o login do usuario para remover: ").strip()

    if login == "admin":
        print("Erro: nao e permitido remover o usuario administrador.")
        return

    usuario = buscar_usuario_por_login(login)
    if usuario is None:
        print("Usuario nao encontrado.")
        return

    usuarios.remove(usuario)
    print("Usuario removido com sucesso!")


def listar_usuarios():
    print("=== LISTA DE USUARIOS ===")
    if len(usuarios) == 0:
        print("Nenhum usuario cadastrado.")
        return

    for i, u in enumerate(usuarios, start=1):
        print(f"{i}. Login: {u['login']} | Nome: {u['nome']}")


def menu_usuarios():
    while True:
        limpar_tela()
        print("=== GERENCIAMENTO DE USUARIOS ===")
        print("1 - Cadastrar usuario")
        print("2 - Pesquisar usuario (por login)")
        print("3 - Remover usuario (por login)")
        print("4 - Listar usuarios")
        print("0 - Voltar")
        opcao = input("Escolha uma opcao: ").strip()

        limpar_tela()
        if opcao == "1":
            cadastrar_usuario()
            pausar()
        elif opcao == "2":
            pesquisar_usuario()
            pausar()
        elif opcao == "3":
            remover_usuario()
            pausar()
        elif opcao == "4":
            listar_usuarios()
            pausar()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")
            pausar()


def fazer_login():
    while True:
        limpar_tela()
        print("=== LOGIN DO SISTEMA ===")
        login = input("Login (ou 'sair' para encerrar): ").strip()
        if login.lower() == "sair":
            return None

        senha = input("Senha: ")
        usuario = buscar_usuario_por_login(login)

        if usuario is not None and usuario["senha"] == senha:
            print(f"\nBem-vindo, {usuario['nome']}!")
            pausar()
            return usuario
        else:
            print("\nLogin ou senha incorretos.")
            pausar()


def menu_principal(usuario_logado):
    while True:
        limpar_tela()
        print(f"=== SISTEMA PRINCIPAL (Logado como: {usuario_logado['login']}) ===")
        print("1 - Gerenciar usuarios")
        print("2 - Trocar de usuario (logout)")
        print("0 - Sair")
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            menu_usuarios()
        elif opcao == "2":
            break
        elif opcao == "0":
            limpar_tela()
            print("Saindo do sistema...")
            return "sair"
        else:
            limpar_tela()
            print("Opcao invalida.")
            pausar()


def main():
    while True:
        usuario = fazer_login()
        if usuario is None:
            limpar_tela()
            print("Programa encerrado.")
            break
        resultado = menu_principal(usuario)
        if resultado == "sair":
            break


if __name__ == "__main__":
    main()
