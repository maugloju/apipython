def arvore_binaria_inserir(no, chave, valor):
    if no is None:
        return TreeNode(None, chave, valor, None)
    if chave == no.chave:
        return TreeNode(no.filho_esquerdo, chave, valor, no.filho_direito)
    if chave < no.chave:
        return TreeNode(arvore_binaria_inserir(no.filho_esquerdo, chave, valor), no.chave, no.valor, no.filho_direito)
    else:
        return TreeNode(no.filho_esquerdo, no.chave, no.valor, arvore_binaria_inserir(no.filho_direito, chave, valor))