import os

def write_project_folder(root_dir, project):
    if not os.path.exists(os.path.join(root_dir, project)):
        os.mkdir(os.path.join(root_dir, project))
    