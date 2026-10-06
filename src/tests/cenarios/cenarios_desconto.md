# Cenários de teste — cálculo de desconto

| ID | Cenário | Entrada: valor e tipo | Resultado esperado |
|---|---|---|---|
| CT01 | Compra de valor zero, cliente comum | `0`, `COMUM` | R$ 0,00 |
| CT02 | Compra logo abaixo de R$ 100, comum | `99.99`, `COMUM` | R$ 0,00 |
| CT03 | Compra logo abaixo de R$ 100, VIP | `99.99`, `VIP` | R$ 5,00 (5%) |
| CT04 | Compra exatamente de R$ 100, comum | `100`, `COMUM` | R$ 10,00 (10%) |
| CT05 | Compra exatamente de R$ 100, VIP | `100`, `VIP` | R$ 15,00 (15%) |
| CT06 | Compra entre R$ 100 e R$ 500, comum | `300`, `COMUM` | R$ 30,00 (10%) |
| CT07 | Compra logo abaixo de R$ 500, comum | `499.99`, `COMUM` | R$ 50,00 apó arredondamento |
| CT08 | Compra exatamente de R$ 500, comum | `500`, `COMUM` | R$ 100,00 (20%) |
| CT09 | Compra exatamente de R$ 500, VIP | `500`, `VIP` | R$ 125,00 (25%) |
| CT10 | VIP escrito em minúsculas | `200`, `vip` | R$ 30,00 (15%) |
| CT11 | VIP com letras mistas | `200`, `Vip` | R$ 30,00 (15%) |
| CT12 | Desconto logo abaixo do teto | `799.96`, `VIP` | R$ 199,99 |
| CT13 | Desconto exatamente no teto | `800`, `VIP` | R$ 200,00 |
| CT14 | Desconto calculado no teto, cliente comum | `1000`, `COMUM` | R$ 200,00 |
| CT15 | Desconto acima do teto | `2000`, `VIP` | R$ 200,00 |
| CT16 | Valor negativo (dado inesperado) | `-0.01` e `-100`, `COMUM` | Lançar `ValueError` |
| CT17 | Valor não numérico (dado inesperado) | `None`, `"100"` e `True` | Lançar `TypeError` |
| CT18 | Tipo de cliente não textual (dado inesperado) | `None` e `123` | Lançar `TypeError` |
| CT19 | Categoria desconhecida (dado inesperado) | `100`, `PREMIUM` | Lançar `ValueError` |

Foram aplicadas partição de equivalência e análise de valor-limite. Para entradas que a história não especifica, foi definido um comportamento seguro: rejeitar o dado explicitamente em vez de devolver um desconto silenciosamente incorreto.
