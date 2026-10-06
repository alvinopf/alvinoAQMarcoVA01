import pytest

from ecommerce.desconto import calcular_desconto


@pytest.mark.parametrize(
    ("valor_compra", "tipo_cliente", "desconto_esperado"),
    [
        # Compras abaixo de R$ 100: 0% para COMUM e 5% para VIP.
        (0, "COMUM", 0.00),
        (99.99, "COMUM", 0.00),
        (99.99, "VIP", 5.00),
        # R$ 100 é o limite inclusivo da faixa de 10%.
        (100, "COMUM", 10.00),
        (100, "VIP", 15.00),
        (100.01, "COMUM", 10.00),
        # Interior e limite superior da faixa de 10%.
        (300, "COMUM", 30.00),
        (499.99, "COMUM", 50.00),
        # R$ 500 inicia a faixa de 20%.
        (500, "COMUM", 100.00),
        (500, "VIP", 125.00),
        (500.01, "COMUM", 100.00),
        # A identificação de VIP não diferencia maiúsculas de minúsculas.
        (200, "vip", 30.00),
        (200, "Vip", 30.00),
        # Valores abaixo, exatamente no teto e acima dele.
        (799.96, "VIP", 199.99),
        (800, "VIP", 200.00),
        (800.01, "VIP", 200.00),
        (1000, "COMUM", 200.00),
        (2000, "VIP", 200.00),
    ],
)
def test_calcular_desconto_regras_de_negocio(
    valor_compra, tipo_cliente, desconto_esperado
):
    # Arrange: dados recebidos do parametrize.

    # Act
    desconto_calculado = calcular_desconto(valor_compra, tipo_cliente)

    # Assert
    assert desconto_calculado == desconto_esperado


@pytest.mark.parametrize("valor_invalido", [-0.01, -100])
def test_rejeita_valor_de_compra_negativo(valor_invalido):
    with pytest.raises(ValueError, match="não pode ser negativo"):
        calcular_desconto(valor_invalido, "COMUM")


@pytest.mark.parametrize("valor_invalido", [None, "100", True])
def test_rejeita_valor_de_compra_nao_numerico(valor_invalido):
    with pytest.raises(TypeError, match="deve ser numérico"):
        calcular_desconto(valor_invalido, "COMUM")


@pytest.mark.parametrize("tipo_invalido", [None, 123])
def test_rejeita_tipo_de_cliente_nao_textual(tipo_invalido):
    with pytest.raises(TypeError, match="deve ser texto"):
        calcular_desconto(100, tipo_invalido)


@pytest.mark.parametrize("tipo_invalido", ["", "   ", "PREMIUM"])
def test_rejeita_categoria_de_cliente_invalida(tipo_invalido):
    with pytest.raises(ValueError, match="COMUM ou VIP"):
        calcular_desconto(100, tipo_invalido)
