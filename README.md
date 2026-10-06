# Desafio prático — Auditoria e Caça aos Bugs

Projeto de testes unitários automatizados para uma função de descontos progressivos de e-commerce.

## Estrutura do projeto

```text
.
├── src/
│   ├── ecommerce/
│   │   ├── desconto.py
│   │   └── desconto_original.py
│   └── tests/
│       ├── cenarios/
│       │   └── cenarios_desconto.md
│       └── test_desconto.py
├── evidencias/
│   ├── PRINT1-antes-da-correcao.png
│   └── PRINT2-apos-a-correcao.png
├── pytest.ini
└── requirements.txt
```

## Arquivos principais

- `src/ecommerce/desconto.py`: implementação corrigida.
- `src/ecommerce/desconto_original.py`: cópia do código recebido do Dev Jr.
- `src/tests/test_desconto.py`: 28 casos automatizados com Pytest.
- `src/tests/cenarios/cenarios_desconto.md`: cenários descritos textualmente.
- `evidencias/`: relatórios e imagens das execuções antes e depois.

## Como executar

No diretório raiz do projeto:

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

O `pytest.ini` adiciona `src` ao caminho de importação e determina que os testes ficam em `src/tests`.

## Estratégia de testes

Foi usado `@pytest.mark.parametrize` porque a função não exige preparação de ambiente: cada caso muda apenas os dados de entrada e o resultado esperado. Os cenários cobrem partições de equivalência, valores-limite, capitalização de `VIP`, teto do desconto, arredondamento e dados inesperados.
