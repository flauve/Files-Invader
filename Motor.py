__author__ = 'florian'
import os

class Motor:

    @staticmethod
    def pollute(path_directory, nbWastingFiles):
        test = "l"
        list_all_dirs_files = os.listdir(path_directory)
        path_before = path_directory + "\\"
        list_files = []
        list_dirs = []
        for file in list_all_dirs_files:
            path = path_before + file
            if file != "__init__.py":
                if os.path.isfile(path):
                    list_files.append(path)
                if os.path.isdir(path):
                    list_dirs.append(path)

        for directory in list_dirs:
            Motor.pollute(directory, nbWastingFiles)

        for file in list_files:
            i = 0
            while i < nbWastingFiles:
                size = os.path.getsize(file)
                file_name = file + str(i)
                f = open(file_name,"w")
                f.seek(size)
                f.write("\0")
                f.close()
                i+= 1