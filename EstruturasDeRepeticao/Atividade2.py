"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do
usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""

class log:
    def login(email, senha, confir_senha):
        print('Crie seu email e sua senha \n')
        email = input('Crie o seu email\n')
        senha = input('Crie a sua senha\n')
        confir_senha = input('Confirme a sua senha\n')

    pass

    while email == senha:
        print('Seu email não pode ser igual a sua senha\n')
        log.login()
    while senha != confir_senha:
        print('Confrimação de senha errada!\n')
        login()
