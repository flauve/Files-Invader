__author__ = 'root'
import unittest
import shutil
import os

from Motor import Motor

class TestMotor(unittest.TestCase):

    TMP_PATH = "tmp"

    def setUp(self):
        if os.path.isdir(self.TMP_PATH):
            shutil.rmtree(self.TMP_PATH)
        os.makedirs(self.TMP_PATH)
        os.rename("__init__.py", self.TMP_PATH + "/__init__.py")
        fichier = open("__init__.py", "w")
        fichier.close()

    def testPollute(self):
        file_name = "mario"
        file = open(self.TMP_PATH + "\\" + file_name, "w")
        file.writelines("luigi")
        file.seek(3000)
        file.write("\0")
        file.close()
        file = open(self.TMP_PATH + "\mario", "w")
        file.writelines("luigi")
        file.close()
        os.makedirs(self.TMP_PATH + "\directory", 20)
        Motor.pollute(self.TMP_PATH, 2)
        self.assertTrue(True)

    def tearDown(self):
        if os.path.isdir(self.TMP_PATH):
            shutil.rmtree(self.TMP_PATH)