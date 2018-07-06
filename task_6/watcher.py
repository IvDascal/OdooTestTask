import json
import os
import shutil
import time

class DirDoesNotExists(Exception):
    pass


class Watcher():
    actions = None
    config = None
    copied_files = []
    copy_path = None
    monitoring_path = None
    move_path = None

    def __init__(self, config_path, base_path=None):
        self.config_path = config_path

        if base_path:
            self.base_path = base_path
        else:
            self.base_path = os.path.dirname(os.path.abspath(__file__))


    def get_config(self):
        path_to_config = os.path.abspath(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                self.config_path)
            )
        try:
            with open(path_to_config) as f:
                self.config = json.load(f)
        except Exception as e:
            print('Could not open: {}\nBecause: {}\n'.format(self.config_path, e))

    def check_paths_exists(self, path_tail):
        if path_tail:
            path = os.path.abspath(
                os.path.join(
                    self.base_path,
                    path_tail)
                )
            if not os.path.exists(path):
                os.makedirs(path)
            return path
        else:
            return None

    def parse_config(self):
        self.get_config()

        self.monitoring_path = self.check_paths_exists(self.config.get('monitoring_path'))
        self.copy_path = self.check_paths_exists(self.config.get('copy_path'))
        self.move_path = self.check_paths_exists(self.config.get('move_path'))

        self.actions = self.config.get('actions')

    def copy_file(self, file_path, file_name):
        if file_name not in self.copied_files:
            shutil.copy(file_path, os.path.join(self.copy_path, file_name))
            self.copied_files.append(file_name)
            print('COPY\t {}'.format(file_name))
    
    def move_file(self, file_path, file_name):
        shutil.move(file_path, os.path.join(self.move_path, file_name))
        print('MOVE\t {}'.format(file_name))

    def delete_file(self, file_path, file_name):
        os.remove(file_path)
        print('DELETED\t {}'.format(file_name))

    def watch(self):
        self.parse_config()

        path_to_watch = os.path.abspath(
            os.path.join(
                self.base_path,
                self.monitoring_path)
            )
        
        print('Start watching directory: {}'.format(path_to_watch))
        if not os.path.isdir(path_to_watch):
            raise DirDoesNotExists

        files_list = os.listdir(path_to_watch)
        
        for file_name in files_list:
            full_file_name = os.path.join(path_to_watch, file_name)
            if (os.path.isfile(full_file_name)):
                file_extension = os.path.splitext(full_file_name)[-1].replace('.', '')
                action = self.actions.get(file_extension)
                
                if action == 'del':
                    self.delete_file(full_file_name, file_name)
                elif action == 'copy':
                    self.copy_file(full_file_name, file_name)
                elif action == 'move':
                    self.move_file(full_file_name, file_name)

        print('Finish watching')


if __name__ == '__main__':
    watcher = Watcher('./config.json')

    while True:
        watcher.watch()
        time.sleep(5)
