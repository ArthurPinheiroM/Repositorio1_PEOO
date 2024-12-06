class CRUD:
        objetos = []    # atributo estático

        @classmethod
        def inserir(cls, obj):
            cls.abrir()
            m = 0
            for c in cls.objetos:
                if c.id > m: m = c.id
            obj.id = m + 1
            cls.objetos.append(obj)
            cls.salvar()

        @classmethod
        def listar_id(cls, id):
            cls.abrir()
            for c in cls.objetos:
                if c.id == id: return c
            return None  
        
        @classmethod
        def atualizar(cls, obj):
            c = cls.listar_id(obj.id)
            if c != None:
                c.nome = obj.nome
                c.email = obj.email
                c.fone = obj.fone
                c.senha = obj.senha
                cls.salvar()

        @classmethod
        def excluir(cls, obj):
            c = cls.listar_id(obj.id)
            if c != None:
                cls.objetos.remove(c)
                cls.salvar()
        
        @classmethod
        def listar(cls):
            cls.abrir()
            cls.objetos.sort(key=lambda cliente: cliente.nome)
            return cls.objetos




# Modelo de salvar do cliente, que muda para cada entidade.👇



#   @classmethod
#   def salvar(cls):
#     with open("clientes.json", mode="w") as arquivo:   # w - write
#       json.dump(cls.objetos, arquivo, default = vars)

#   @classmethod
#   def abrir(cls):
#     cls.objetos = []
#     try:
#       with open("clientes.json", mode="r") as arquivo:   # r - read
#         texto = json.load(arquivo)
#         for obj in texto:   
#           c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
#           cls.objetos.append(c)
#     except FileNotFoundError:
#       pass
