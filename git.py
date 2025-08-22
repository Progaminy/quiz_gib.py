questoes = [{
    "pergunta": "passo 1. intalar o git",
    "resposta": "pkg install git"
},
{
    "pergunta": "passo 2 verifique a versao ou se esta funcionando",
    "resposta": "git --version"
},
{
    "pergunta": "PASSO 3 – Configurar seu Git com nome e e-mail: ",
    "resposta": "git config --global user.name 'progaminy',git config --global user.email 'adaddasmaravilhas@gmail.com'",
},
{
    "pergunta": "PASSO 4 - verifique se ja esta adicionado na lista",
    "resposta": "git config --list"
},
{
    "pergunta":" PASSO 5 – Criar ou usar uma conta no GitHub",
    "resposta": "https://github.com/"
},
{
    "pergunta": "PASSO 6 - Crie um novo repositório com o nome, por exemplo: ",
    "resposta": "meusite"
},
{
    "pergunta": "PASSO 7 - Copie a URL do seu repositório. ",
    "resposta": "https://github.com/progaminy/meusite.git"
},
{
    "pergunta": "PASSO 8 - Clonar o repositorio ja cm link copiado",
    "resposta": "git clone,https://github.com/progaminy/meusite.git"
},
{
    "pergunta": "PASSO 9 - entre na pasta clonada",
    "resposta": "cd meusite"
},
{
    "pergunta": "PASSO 10 - criar token acesso pessoal (PAT8): ",
    "resposta": "https://github.com/settings/tokens"
},
{
    "pergunta": "PASSO 11 - enviar projecto para o GitHub (push)",
    "resposta": "git add .,git commit -m 'editado',git push"
}]

for a in questoes:
    while True:
        answer_user = input(a['pergunta'])
        if answer_user == a["resposta"]:
            print(f"Acertou, ")
            break
        else:
            print(f"Errou, tente novamente, a resposta seria : {a['resposta']}")

print("fim")


