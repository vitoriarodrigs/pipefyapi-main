from schemas.schemas import PessoaCreate
from clients.pipefy_client import execute_graphql, PIPE_ID
from enums.cidade_enum import Cidade
from enums.phase_enum import Phase

def _validate_cidade(cidade_id: str) -> dict | None:
    cidades_validas = [cidade.value for cidade in Cidade]
    
    if cidade_id not in cidades_validas:
        cidades_disponiveis = [
            {"id": cidade.value, "nome": cidade.nome}
            for cidade in Cidade
        ]
        return {
            "erro": f"Cidade com ID '{cidade_id}' não encontrada",
            "cidades_disponiveis": cidades_disponiveis
        }
    
    return None

def _validate_phase(phase_id: str) -> dict | None:
    phases_validas = [phase.value for phase in Phase]
    
    print(f"Phases válidas: {phases_validas}, Phase recebida: {phase_id}")
    if phase_id not in phases_validas:
        phases_disponiveis = [
            {"id": phase.value, "nome": phase.nome}
            for phase in Phase
        ]
        return {
            "erro": f"Phase com ID '{phase_id}' não encontrada",
            "phases_disponiveis": phases_disponiveis
        }
    
    return None

def _build_fields(pessoa: PessoaCreate):
    fields = [
        {"field_id": "nome", "field_value": pessoa.nome},
        {"field_id": "cidade", "field_value": [pessoa.cidade_id]}
    ]
    
    
    if pessoa.data_de_nascimento:
        fields.append({
            "field_id": "data_de_nascimento",
            "field_value": pessoa.data_de_nascimento.isoformat()
        })
    
    if pessoa.cpf:
        fields.append({
            "field_id": "cpf",
            "field_value": pessoa.cpf
        })
    
    if pessoa.telefone:
        fields.append({
            "field_id": "telefone",
            "field_value": pessoa.telefone
        })
    
    if pessoa.data_envio:
        fields.append({
            "field_id": "data",
            "field_value": pessoa.data_envio.isoformat()
        })
    
    if pessoa.sexo:
        fields.append({
            "field_id": "sexo",
            "field_value": pessoa.sexo
        })
    
    if pessoa.hobbies:
        fields.append({
            "field_id": "hobbies",
            "field_value": pessoa.hobbies
        })
    
    return fields

def create_card(pessoa: PessoaCreate):
    erro_cidade = _validate_cidade(pessoa.cidade_id)
    if erro_cidade:
        return erro_cidade
    
    query = """
    mutation ($pipe_id: ID!, $fields: [FieldValueInput!]!) {
      createCard(input: {
        pipe_id: $pipe_id,
        fields_attributes: $fields
      }) {
        card {
          id
          title
        }
      }
    }
    """

    variables = {
        "pipe_id": PIPE_ID,
        "fields": _build_fields(pessoa)
    }

    result = execute_graphql(query, variables)
    return result

def delete_card(card_id: int):
    query = """
    mutation ($id: ID!) {
      deleteCard(input: {id: $id}) {
        success
      }
    }
    """

    return execute_graphql(query, {"id": card_id})

def move_card(card_id: int, phase_id: int):
    erro_phase = _validate_phase(phase_id)
    if erro_phase:
        return erro_phase
    query = """
    mutation ($card_id: ID!, $phase_id: ID!) {
      moveCardToPhase(input: {
        card_id: $card_id,
        destination_phase_id: $phase_id
      }) {
        card {
            current_phase {
                id
                name
            }
        }
      }
    }
    """

    result = execute_graphql(query, {"card_id": card_id, "phase_id": phase_id})
    if(result.get("errors")):
        return {
            "erro": result["errors"][0]["message"]
        }
    current_phase = result["data"]["moveCardToPhase"]["card"]["current_phase"]

    if current_phase["id"] == Phase.CONCLUIDO.value:
        return {
            "message": "Card movido para fase final",
            "phase": current_phase["name"]
        }
    
    return {
        "message": "Card movido com sucesso",
        "phase": current_phase["name"]
    }
