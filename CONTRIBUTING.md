# Guia de Contribuições para `1º Desafio de Dados - Ciência de Dados em Recursos Humanos` 🎉

Obrigado por considerar contribuir para o nosso projeto! Para mantermos um ambiente de trabalho organizado e eficiente, por favor, siga estas diretrizes ao contribuir.

## Nomenclatura das Branches 🌿

- Use a convenção `tipo/descrição-curta` para nomear suas branches.
- Tipos comuns incluem:
  - `feature`: Para novas funcionalidades.
  - `bugfix`: Para correções de bugs.
  - `hotfix`: Para correções urgentes em produção.
  - `refactor`: Para melhorias e refatorações de código.
- Exemplos:
  - `feature/adicionar-analise-de-correlação`
  - `bugfix/corrigir-importacao-dados`
  - `hotfix/ajuste-calculo-turnover`

## Nomes dos Commits 📝

- Use mensagens de commit descritivas e concisas.
- Siga a convenção `tipo: descrição breve`.
- Tipos comuns:
  - `feat`: Uma nova funcionalidade.
  - `fix`: Correção de um bug.
  - `docs`: Alterações na documentação.
  - `style`: Mudanças que não afetam a lógica (ex.: formatação).
  - `refactor`: Alterações de código que melhoram o desempenho ou legibilidade.
  - `test`: Adição ou modificação de testes.
  - `chore`: Outras mudanças que não se enquadram nos tipos acima.
- Exemplos:
  - `feat: adicionar análise de correlação`
  - `fix: corrigir erro na importação de dados`
  - `docs: atualizar README com novas instruções`
  - `style: formatar código de visualização`

## Nomes dos Arquivos 📄

- Use nomes de arquivos descritivos e em `snake_case`.
- Exemplos:
  - `prepare_data.py`
  - `correlation_analysis.py`
  - `turnover_model.py`
  - `visualize_data.py`

## Estrutura do Código 🏗️

- Organize seu código de acordo com a estrutura de diretórios estabelecida:
```plaintext
desafio_dados_rh/
│
├── data/                # Dados brutos e processados
│   ├── raw/             # Dados brutos
│   └── processed/       # Dados processados
│
├── notebooks/           # Notebooks Jupyter para análises exploratórias e modelagem
│
├── src/                 # Código fonte dos modelos e análises
│   ├── data_preparation/ # Scripts de preparação dos dados
│   │   └── prepare_data.py
│   ├── analysis/         # Scripts de análises estatísticas
│   │   └── correlation_analysis.py
│   ├── models/           # Scripts de modelagem
│   │   └── turnover_model.py
│   └── visualization/    # Scripts para visualização dos dados
│       └── visualize_data.py
│
├── reports/             # Relatórios e resultados finais
│
├── requirements.txt     # Lista de dependências do projeto
│
└── README.md            # Descrição do projeto

```

- Mantenha a organização e limpeza do código.
- Documente funções e classes com docstrings.

## Padrões de Código 🧑‍💻

- Siga o PEP 8 para estilo de código Python.
- Use comentários para explicar partes complexas do código.
- Teste suas mudanças antes de comitar.

## Processo de Pull Request 🔄

1. **Faça um fork do repositório e clone o repositório forkado.**
2. **Crie uma nova branch para sua feature ou correção.**
3. **Implemente suas mudanças, seguindo as diretrizes acima.**
4. **Comite suas mudanças com mensagens de commit apropriadas.**
5. **Envie suas mudanças para o repositório forkado.**
6. **Abra um Pull Request detalhando suas mudanças.**

## Checklist de Pull Request ✅

- [ ] O código segue os padrões de estilo e contribuições.
- [ ] As mudanças foram testadas e estão funcionando corretamente.
- [ ] A documentação foi atualizada conforme necessário.
- [ ] O Pull Request está descrito de maneira clara e concisa.

## Comunidade e Suporte 👐

- Use a aba "Issues" do GitHub para reportar bugs, solicitar funcionalidades ou iniciar discussões.
- Respeite todos os colaboradores e siga o código de conduta do projeto.

Obrigado por contribuir para o `1º Desafio de Dados - Ciência de Dados em Recursos Humanos`! Juntos, podemos criar soluções inovadoras para Recursos Humanos utilizando ciência de dados.

