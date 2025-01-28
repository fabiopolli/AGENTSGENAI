from flask import Blueprint, request, jsonify
from src.workflows.genai_workflow import genai_flow

bp = Blueprint("api", __name__)

@bp.route("/chat", methods=["POST"])
def chat():
    """
    Endpoint para processar as perguntas do usuário e retornar a resposta correta.
    """
    data = request.get_json()
    user_input = data.get("question", "")

    response = genai_flow(user_input)

    return jsonify({"response": response})
