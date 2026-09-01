# ⚡ CodePulse

> Analisador de projetos de código com foco em métricas, qualidade e saúde do projeto.

O **CodePulse** é um projeto de portfólio desenvolvido em Python com o objetivo de analisar projetos de software e transformar informações do código em métricas e alertas úteis.

A ideia é começar com um analisador local simples e evoluir gradualmente para uma ferramenta capaz de analisar repositórios do GitHub, identificar problemas e apresentar os resultados de forma clara.

---

## 🎯 Objetivo

O CodePulse pretende responder perguntas como:

- Quantos arquivos existem no projeto?
- Quais linguagens são utilizadas?
- Quantas linhas de código existem?
- Existem arquivos ou funções muito grandes?
- Qual é a complexidade do código?
- A documentação está adequada?
- Existem possíveis problemas de segurança?
- Existem dependências desatualizadas?
- Como está a estrutura geral do projeto?

---

## 🚧 Status

**Em desenvolvimento — Fase inicial**

Atualmente estamos construindo o núcleo do analisador.

### Já implementado

- [x] Estrutura inicial do projeto
- [x] Recebimento de um caminho de projeto
- [x] Conversão do caminho para `pathlib.Path`
- [x] Leitura do conteúdo de diretórios
- [x] Identificação de arquivos e diretórios
- [x] Busca recursiva em subdiretórios

### Próximos passos

- [ ] Ignorar diretórios desnecessários (`.git`, `venv`, `node_modules`, etc.)
- [ ] Coletar arquivos Python
- [ ] Contar linhas de código
- [ ] Criar primeiras métricas
- [ ] Organizar os resultados
- [ ] Criar testes automatizados
- [ ] Criar API com FastAPI
- [ ] Integrar análise de repositórios GitHub
- [ ] Adicionar análise com AST
- [ ] Criar sistema de pontuação do projeto
- [ ] Criar dashboard

---

## 🧠 Como o CodePulse funciona

A arquitetura será construída gradualmente.

```text
Projeto
   │
   ▼
Scanner
   │
   ├── Arquivos
   ├── Diretórios
   └── Estrutura
          │
          ▼
      Analisadores
          │
          ├── Código
          ├── Complexidade
          ├── Documentação
          └── Segurança
                  │
                  ▼
               Métricas
                  │
                  ▼
             Project Score
                  │
                  ▼
              Dashboard