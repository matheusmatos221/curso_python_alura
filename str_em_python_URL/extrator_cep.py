endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re # Regular Expressions -- RegEx

# 5 dígitos + hífen (opcional) + 3 dígitos

"""Declara o padrão completo"""
# padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789]")

"""Declara se alguma pode ser opcional"""
# padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")

"""Declara o padrão n vezes repetidas"""
# padrao = re.compile("[0123456789]{5}[-]?[0123456789]{3}")

"""Declara o intervalo do padrão"""
# padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")

"""Declara quantas vezes o valor pode aparecer no padrão"""
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}") # também é possível usar [a-z]
busca = padrao.search(endereco) # Match

if busca:
    cep = busca.group()
    print(cep)