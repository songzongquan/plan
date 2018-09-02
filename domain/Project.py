
class Project:
    def __init__(self,id,name,memo,owner,projectDao):
        self.id = id
        self.name =  name
        self.memo = memo
        self.owner =  owner
        self.projectDao = projectDao

    def __init__(self,projectDao):
        self.projectDao = projectDao 
    
    def getId(self):
        return self.id
    def setId(self,id):
        self.id = id
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
    def getMemo(self):
        return self.memo
    def setMemo(self):
        self.memo = memo
    def getOwner(self):
        return self.owner
    def setOwner(self,owner):
        self.owner = owner

    def create(self,project):
        return self.projectDao.save(project)
    def read(self,id):
        return self.projectDao.load(id)
    def update(self,project):
        return self.projectDao.update(project)
    def delete(self,id):
        return self.projectDao.delete(id)
    def findAll(self):
        return self.projectDao.findAll()

