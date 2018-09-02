from app import app
from domain.Project import Project
from domain.ProjectDao import ProjectDao
from persistent.ProjectDaoImpl import ProjectDaoImpl
import unittest

class AppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing =  True

    def test_project(self):
        result = self.app.get('/api/v1/project/7')
        self.assertEquals(result.status_code,200)
