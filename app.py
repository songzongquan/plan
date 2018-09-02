from flask import Flask
from flask import jsonify
import json
from flask import request
from flask import abort

from flask import render_template

from domain.Project import Project

from  domain.ProjectDao import ProjectDao
from persistent.ProjectDaoImpl import ProjectDaoImpl
 

app = Flask(__name__)


@app.route('/api/v1/project/<int:id>',methods=['GET'])
def getProjectById(id):
    project = getProject()
    data = project.read(id)
    if data:
        result ={}
        result['id'] =  data.id
        result['name']= data.name
        result['memo'] = data.memo
        result['owner'] = data.owner
        return jsonify(result),200
    else:
        abort(404)

@app.route("/api/v1/project",methods=['POST'])
def addProject():
    project =  getProject()
    if not request.json or not 'id' in request.json or not 'name' in request.json:
        abort(400)
    project.id= request.json['id']
    project.name = request.json['name']
    project.memo = request.json['memo']
    project.owner = request.json['owner']

    result = project.create(project)
    print(result)
    if result == 1:
        return jsonify({'status':'success'}),201
    elif result ==0:
        abort(409)
    else:
        abort(500)
@app.route('/api/v1/project/<int:id>',methods=['DELETE'])
def removeProject(id):
    project = getProject()
    result = project.delete(id)
    print(result)
    if result == 1:
        return jsonify({'status':'success'}),200
    elif result == 0:
        abort(404)
    else:
        abort(500)

@app.route('/api/v1/project/<int:id>',methods=['PUT'])
def modifyProject(id):
    project = getProject()
    project = project.read(id)
    if not request.json:
        abort(400)
    if 'name' in request.json:
        project.name = request.json['name']
    if 'memo' in request.json:

        project.memo = request.json['memo']
    if 'owner' in request.json:
        project.owner = request.json['owner']
    print(project.name)    
    result = project.update(project)
    if result == 0:
        abort(404)
    elif result ==1:
        return jsonify({'status':'success'}),200

@app.route('/api/v1/projects',methods=['GET'])
def findAllProject():
    project = getProject()
    projects = project.findAll()
    result = []
    if len(projects) !=0:
        for p1 in projects:
            p ={}
            p['id'] = p1.id
            p['name'] =p1.name
            p['memo'] = p1.memo
            p['owner'] = p1.owner
            result.append(p)

    return jsonify(result),200

def getProject():
    dao = ProjectDaoImpl()
    project =  Project(dao)
    return project

@app.route('/add_project')
def add_project():
    return render_template('add_project.html')
@app.route('/project_list')
def list_project():
    return render_template('project_list.html')
@app.route('/edit_project')
def edit_project():
    id = request.args['id']
    return render_template('edit_project.html',id=id)

