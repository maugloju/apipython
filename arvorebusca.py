# 'no' refere-se ao nó-pai, neste caso
def arvore_binaria_buscar(no, valor):
    if no is None:
        # valor não encontrado
        return None
    else:
        if valor == no.valor:
            # valor encontrado
            return no.valor
        elif valor < no.valor:
            # busca na subárvore esquerda
            return arvore_binaria_buscar(no.filho_esquerdo, valor)
        elif valor > no.valor:
            # busca na subárvore direita
            return arvore_binaria_buscar(no.filho_direito, valor)