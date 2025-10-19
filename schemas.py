from pydantic import BaseModel
from typing import Optional,List

#os schemas sao usados para padronizar a Validação de Dados de Entrada (Requisições) e a Serialização de Dados de Saída (Respostas)

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]

    class Config:
        from_attributes = True

class PedidoSchema(BaseModel):
    id_usuario: int

    class Config:
        from_attributes = True

class LoginSchema(BaseModel):
    email: str
    senha: str

    class Config:
        from_attributes = True

class ItemPedidoSchema(BaseModel):
    quantidade:int
    sabor:str
    tamanho:str
    preco_unitario:float

    class Config:
        from_attributes = True

class ResponsePedidosSchema(BaseModel):
    id:int
    status:str
    preco:float

    class Config:
        from_attributes = True
