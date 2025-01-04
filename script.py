import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer

# configurando a engine do BD
engine = create_engine("sqlite:///database.db")

# configurando a sessão
Session = sessionmaker(engine)

# criando a tabela
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    tipo = Column(String, nullable=False)

def insert_usuario(nome_usuario, tipo_usuario):
    session = Session()
    try:
        if all([nome_usuario, tipo_usuario]):
            usuario = Usuario(nome=nome_usuario, tipo=tipo_usuario)
            session.add(usuario)
            session.commit()
            print(f'Usuário {nome_usuario} cadastrado com sucesso!')
        else:
            print('É obrigatório preencher o nome e o tipo do usuário!')
    except Exception as e:
        session.rollback()
        print(f'Ocorreu um erro ao tentar cadastrar o usuário {nome_usuario}: {e}')
    finally:
        session.close()

def select_usuarios(nome_usuario=''):
    session = Session()  # Criando a sessão aqui
    try:
        if nome_usuario:
            dados = session.query(Usuario).filter(Usuario.nome == nome_usuario)
        else:
            dados = session.query(Usuario).all()

        for i in dados:
            print(f'Usuário: {i.nome} - Tipo: {i.tipo}')
    except Exception as e:
        print('Ocorreu algum erro ao consultar o(s) usuario(s):', e)
    finally:
        session.close()
def update_nome_usuario(id_usuario, nome_usuario):
    session = Session()
    try:
        if all([id_usuario, nome_usuario]):
            usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
            if usuario:  # Verificando se o usuário foi encontrado
                usuario.nome = nome_usuario
                session.commit()
                print('Nome do usuário atualizado com sucesso!')
            else:
                print(f'Usuário com ID {id_usuario} não encontrado!')
        else:
            print('É obrigatório informar o id e o novo nome do usuário!')
    except Exception as e:
        session.rollback()
        print(f'Ocorreu um erro ao atualizar o usuário: {e}')
    finally:
        session.close()

def delete_usuario(id_usuario):
    session = Session()
    try:
        if id_usuario:
            usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
            session.delete(usuario)
            session.commit()
            print(f'Usuário de ID {id_usuario} deletado com sucesso!')
        else:
            print('É obrigatório informar o ID do usuário a ser deletado')
    except Exception as e:
        session.rollback()
        print(f'Erro ao tentar deletar o usuário de ID {id_usuario}!')
    finally:
        session.close()


if __name__ == '__main__':
    os.system('cls')
    Base.metadata.create_all(engine)
    # Descomente a linha abaixo para inserir um usuário
    # insert_usuario('Luky', 'Convidado comum')  
    select_usuarios('Goku')  # Chamando a função corretamente
    # update_nome_usuario(2, 'Vegeta')
    # delete_usuario(2)

