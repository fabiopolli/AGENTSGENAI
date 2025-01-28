import os

use_llamaguard = os.getenv("USE_LLAMAGUARD", "False").lower() == "true"

if use_llamaguard:
    from llamaguard import Moderation
    moderation = Moderation()

    def moderate_content(content):
        result = moderation.check(content)
        if result["flagged"]:
            return "Conteúdo bloqueado por políticas de segurança."
        return content
else:
    print("LlamaGuard está desativado. Nenhuma moderação será aplicada.")

    def moderate_content(content):
        return content  # Apenas retorna o conteúdo sem moderação
