# ⚡ Projeto funcionando:

http://15.229.35.117 (Instância EC2 da AWS)

https://sistema-de-candidaturas.leudoneto.repl.co (Replit)

# 🏷️ Documentação do projeto

## 🚀 Instalação

>  git clone https://github.com/LeudoNeto/sistema-de-candidaturas.git


## 💻 Execução

> 
> - ` 1. ` cd sistema-de-candidaturas
>
> - ` 2. ` python3 manage.py runserver 80
>
> - ` 3. ` No seu `navegador` acesse `http://localhost`.

# 🎥 Testes funcionando:

## Acessando como Empresa:

![Empresa](videos_testes/empresa.gif)

## Acessando como Candidato:

![Candidato](videos_testes/candidato.gif)

# Sobre o projeto

## O Desafio

Criar um site de divulgação de vagas de emprego. Considere dois usuários. Obrigatório o cadastro com email (username = email) e senha.

<ol>
    <li>Empresa deve criar uma (ou várias) vagas.</li>
    <li>Candidato deve se candidatar a uma (ou mais) vagas.</li>
</ol>

A **vaga** que a empresa vai criar deve ter:

<ul>
    <li>Nome da vaga</li>
    <li>Faixa salarial:
        <ul>
            <li>Até 1.000</li>
            <li>De 1.000 a 2.000</li>
            <li>De 2.000 a 3.000</li>
            <li>Acima de 3.000</li>
        </ul>
    </li>
    <li>Requisitos</li>
    <li>Escolaridade mínima:
        <ul>
            <li>Ensino fundamental</li>
            <li>Ensino médio</li>
            <li>Tecnólogo</li>
            <li>Ensino Superior</li>
            <li>Pós / MBA / Mestrado</li>
            <li>Doutorado</li>
        </ul>
    </li>
</ul>

O **candidato** deve informar:

<ul>
    <li>Pretensão salarial</li>
    <li>Experiência</li>
    <li>Última Escolaridade</li>
</ul>

**Objetivo**:

<ol>
    <li>Tela de vagas com número de candidatos
        <ul><li>Ser possível acessar quais candidatos (todos os dados) estão na vaga</li></ul>
    </li>
    <li>Considere que a empresa tem o poder de editar ou deletar as vagas.</li>
    <li>Conseguir pontuar quais candidatos estão dentro do perfil da vaga (faixa salarial + escolaridade). Ex:
        <ul>
            <li>Candidatos = 0 pontos
                <ol>
                    <li>Se dentro da faixa salarial, adiciona 1 ponto</li>
                    <li>Se dentro ou acima da escolaridade, adiciona 1 ponto</li>
                </ol>
            </li>
        <ul>
    </li>
</ol>