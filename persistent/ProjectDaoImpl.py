#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
from domain.ProjectDao import ProjectDao
from domain.Project import Project
class ProjectDaoImpl(ProjectDao):

    
    def load(self,id):
        db = self.getDbconnection()
        cursor =  db.cursor()
        sql = "select * from project where id= %s "
        cursor.execute(sql,(id,))
        print(sql)
        results = cursor.fetchall()
        if len(results) != 0:
            p = Project(self)
            p.id = results[0][0]
            p.name = results[0][1]
            p.memo  = results[0][2]
            p.owner  = results[0][3]
        
            db.close()
            return p
        else:
            db.close()
            return None



    def save(self,project):
        db =  self.getDbconnection()
        cursor =  db.cursor()
        sql =  "select * from project where name = %s and id= %s"
        cursor.execute(sql,(project.name,project.id,))
        data = cursor.fetchall()
        if len(data) != 0:
            db.close()
            return 0
        else:
            sql =  "insert into project (id,name,memo,owner) values(%s,%s,%s,%s)"
            cursor.execute(sql,[project.id,project.name,project.memo,project.owner])
            db.commit()
            print(sql)
            db.close()
            return 1

    def update(self,project):
        
        old_project =  self.load(project.id)
        if not old_project:
            return 0
        db = self.getDbconnection()
        cursor = db.cursor()
        sql = "update project set name= %s,memo = %s,owner = %s where id = %s"
        cursor.execute(sql,(project.name,project.memo,project.owner,project.id))
        db.commit()
        db.close()
        return 1

    def delete(self,id):
        db = self.getDbconnection()
        cursor =  db.cursor()
        sql = "select * from project where id = %s "
        cursor.execute(sql,(id,))
        data = cursor.fetchall()
        if len(data) == 0:
            db.close()
            return 0
        
        sql = "delete from project where id = %s "
        cursor.execute(sql,(id,))
        db.commit()
        db.close()
        return 1
    def findAll(self):
        db = self.getDbconnection()
        cursor = db.cursor()
        sql = "select * from project "
        cursor.execute(sql)
        data = cursor.fetchall()
        projects = []
        if len(data) !=0:
            for row in data:
                p = Project(self)
                p.id = row[0]
                p.memo = row[1]
                p.name = row[2]
                p.owner = row[3]
                projects.append(p)
            return projects
        return None
            
    def getDbconnection(self):       #连接数据库
        
        db = pymysql.connect("localhost","root","123456","pm",charset='utf8')
        return db

