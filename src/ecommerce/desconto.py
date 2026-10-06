def calcular_desconto(valor_compra, tipo_cliente):
    """Retorna, em reais, o desconto aplicável à compra."""
    if isinstance(valor_compra, bool) or not isinstance(valor_compra, (int, float)):
        raise TypeError("O valor da compra deve ser numérico.")
    if valor_compra < 0:
        raise ValueError("O valor da compra não pode ser negativo.")
    if not isinstance(tipo_cliente, str):
        raise TypeError("O tipo de cliente deve ser texto.")

    tipo_normalizado = tipo_cliente.upper()
    if tipo_normalizado not in ("COMUM", "VIP"):
        raise ValueError("O tipo de cliente deve ser COMUM ou VIP.")

    if valor_compra >= 500:
        percentual_desconto = 0.20
    elif valor_compra >= 100:
        percentual_desconto = 0.10
    else:
        percentual_desconto = 0.0

    if tipo_normalizado == "VIP":
        percentual_desconto += 0.05

    valor_desconto = valor_compra * percentual_desconto
    valor_desconto = min(valor_desconto, 200.0)

    return round(valor_desconto, 2)
