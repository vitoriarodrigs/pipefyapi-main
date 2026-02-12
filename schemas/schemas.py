from pydantic import BaseModel, Field, field_validator
from datetime import date, datetime
from typing import Optional, List
from enum import Enum

class SexoEnum(str, Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"
    OUTRO = "Outro"

class PessoaCreate(BaseModel):
    nome: str = Field(..., min_length=1, description="Nome da pessoa")
    cidade_id: str = Field(..., description="ID da cidade (connector)")
    data_de_nascimento: Optional[date] = Field(None, description="Data de nascimento")
    cpf: Optional[str] = Field(None, description="CPF da pessoa")
    telefone: Optional[str] = Field(None, description="Telefone da pessoa")
    data_envio: Optional[datetime] = Field(None, description="Data e hora de envio")
    sexo: Optional[SexoEnum] = Field(None, description="Sexo da pessoa")
    hobbies: Optional[List[str]] = Field(None, description="Lista de hobbies")
    
    @field_validator('cpf')
    @classmethod
    def validate_cpf(cls, v):
        if v is None:
            return v
        cpf_clean = ''.join(filter(str.isdigit, v))
        if len(cpf_clean) != 11:
            raise ValueError('CPF deve conter 11 dígitos')
        return v
    
    @field_validator('telefone')
    @classmethod
    def validate_telefone(cls, v):
        if v is None:
            return v
        telefone_clean = ''.join(filter(str.isdigit, v))
        if len(telefone_clean) not in [10, 11]:
            raise ValueError('Telefone deve conter 10 ou 11 dígitos')
        return v
    
    class Config:
        use_enum_values = True