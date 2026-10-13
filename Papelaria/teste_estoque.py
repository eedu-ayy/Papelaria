from estoque import eh_numero, validar_produto

assert eh-numero("24,90")
assert eh_numero("3")
assert not eh_numero("dez")
assert not eh_numero("-5")

assert validar_produto("Caderno", "24,90", "15") == []
assert validar_produto("Caderno", "0", "15") == ["O vpreço precisa ser um número maior que zero."]
assert len(validar produto("", "abc", "1,5")) == 3
assert validar-produto("Lapis", "1.50", "0") == []

print("")
