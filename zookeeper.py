from turtle import onscreenclick
from treelib import Node,Tree

class Ztree:
    def __init__(self):
        self.tree = Tree()
        self.tree.create_node("/","/")
    
    def get_tree(self):
        return self.tree

    def create(self,path,data,ephemeral,OnService,timeDead,parent):
        
        if(ephemeral):
            self.tree.add_node(Node(path,path,data= Znode(path,data,ephemeral,OnService,timeDead)),parent= parent) 
        else:
            self.tree.add_node(Node(path,path,data= Znode(path,data,ephemeral,OnService,None)),parent= parent)

    def delete(self,path,version):
        if(self.exist(path)):
            nodo = self.tree.get_node(path)
            nodoData = nodo.data
            if(nodoData.ephemeral == False):
                if(self.tree.contains(path)):
                    if(nodoData.version == version):
                        self.tree.remove_node(path)
                    else:
                        print("Las versiones no concuerdan c:")
                        raise Exception()
            else:
                if((nodoData.OnService == False) and (nodoData.ephemeral == True)):
                    self.tree.remove_node(path)
                    return 0
                else:
                    if((nodoData.OnService == True) and (nodoData.ephemeral == True)):
                        for i in range(nodoData.timeDead,-1,-1):
                            if(i == 0):
                                if(nodoData.version == version):
                                    self.tree.remove_node(path)
                                else:
                                    print("Las versiones no concuerdan c:")
                                    raise Exception()
                            else:
                                print("Tiempo restante de vida = {i}".format(i=i))
        else:
            print("Nodo no existe")
            raise Exception()

    def exist(self,path):
        if(self.tree.contains(path)):
            return True
        else: 
            return False
    
    def showTree(self):
        print("\t\t -------Estado actual del Arbol--------")
        self.tree.show()
    
    def getData(self,path):
        if(self.exist(path)):
            nodo = self.tree.get_node(path)
            nodoData = nodo.data
            return(nodoData.data)
        else:
            print("Nodo no existe")
            raise Exception()
    
    def setData(self,path,contenido):
        if(self.exist(path)):
            nodotemp = self.tree.get_node(path)
            nodo = nodotemp.data
            nodo.data = contenido
            nodo.version = nodo.version + 1
        else:
            print("Nodo no existe")
            raise Exception()
    
    def showNode(self,path):
        if(self.exist(path)):
            nodotemp = self.tree.get_node(path)
            nodo = nodotemp.data
            nodo.get_node_info()
        else:
            print("Nodo no existe")
            raise Exception()
    
    def getChildren(self,path):
        if(self.exist(path)):
            nodotemp = self.tree.get_node(path)
            print(self.tree.children(path))
        else:
            print("Nodo no existe")
            raise Exception()
    

    




class Znode:
    def __init__(self,path,data,ephemeral,OnService,timeDead):
        self.path = path
        self.ephemeral = ephemeral
        self.data = data
        self.node = Node(path,path)
        self.OnService = OnService 
        self.timeDead = timeDead
        self.version = 0
    
    def get_node_info(self):
        print("\t \t------ZNode information--------\t\t \n")
        print("Path = {path} ".format(path = self.path))
        print("Ephemeral = {ephemeral} ".format(ephemeral = self.ephemeral))
        print("Version = {version} ".format(version = self.version))
        print("Data = {data} ".format(data = self.data))

        
        
        
        
