import os
import inspect
import importlib.util
import subprocess
import tempfile
import ast

class FunctionOrClass:
    def __init__(self, name, type_, description):
        self.name = name
        self.type = type_  # "function" or "class"
        self.description = description

class Module:
    def __init__(self, name):
        self.name = name
        self.elements = []  # this will contain instances of FunctionOrClass

    def add_element(self, element):
        self.elements.append(element)

class File:
    def __init__(self, name):
        self.name = name
        self.modules = []  # this will contain an instance of Module

    def set_module(self, module):
        self.modules.append(module)

class Folder:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.folders = []

    def add_file(self, file):
        self.files.append(file)

    def add_folder(self, folder):
        self.folders.append(folder)

class Library:
    def __init__(self, name, repo_url):
        self.name = name
        self.temp_dir = tempfile.TemporaryDirectory()
        subprocess.run(["git", "clone", repo_url, self.temp_dir.name], check=True)
        self.root = self.temp_dir.name
        self.files = []
        self.folders = []
        self._populate()

    def _populate(self):
        for root_, dirs, files in os.walk(self.root):
            relative_root = os.path.relpath(root_, self.root)
            if relative_root == ".":
                current_folder = self
            else:
                current_folder = Folder(relative_root)
                self.folders.append(current_folder)

            for file_name in files:
                if file_name.endswith(".py"):
                    file_path = os.path.join(root_, file_name)
                    file = self._create_file(file_path)
                    current_folder.files.append(file)

    def _create_file(self, path):
        file_name = os.path.basename(path)
        file = File(file_name)
        # Import the module from the given file
        spec = importlib.util.spec_from_file_location(file_name, path)
        module_obj = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module_obj)
        # Create a module and add it to the file
        module = Module(file_name)
        file.set_module(module)
        # Use AST to iterate over all classes and functions in the module
        tree = ast.parse(open(path).read())
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                name = node.name
                type_ = type(node).__name__
                # TODO: You might want to extract a description from the docstring or elsewhere
                description = ast.get_docstring(node)
                element = FunctionOrClass(name, type_, description)
                module.add_element(element)
        return file

    def get_overview(self):
        overview = f"Library {self.name} contains:\n"
        folders = [(folder, 1) for folder in self.folders]  # (folder, depth)
        files = [file for file in self.files]
        while folders:
            folder, depth = folders.pop(0)
            overview += "    " * depth + f"Folder: {folder.name}\n"
            
            # Add this folder's files and sub-folders to our lists
            files.extend(folder.files)
            folders.extend((sub_folder, depth + 1) for sub_folder in folder.folders)
        for file in files:
            overview += f"File: {file.name}\n"
            for module in file.modules:
                overview += f"    Module: {module.name}\n"
                for element in module.elements:
                    overview += f"        {element.type.capitalize()}: {element.name}\n"
        return overview

