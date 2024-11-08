import os
import subprocess
import time
from config import log
from pywinauto import Application


class AppTester:
    def __init__(self, app_path):
        self.app = Application('win32')
        self._start(app_path)

    def _start(self, app_path):
        log.warning(app_path)
        # subprocess.run(['start', '/a', 'admin', app_path], check=True)
        try:
            self.app.start(app_path, 5, 3)

            # self.app = Application('uia').connect(title='Kzb Player') #Toggle button.exe
            self.app.connect(path=app_path)
            # self.app = Application().connect(title='Toggle button.exe', visible_only=True) #Toggle button.exe
            # self.app = Application(backend='win32').connect(title=os.path.basename(app_path)) #Toggle button.exe
        except Exception as e:
            raise Exception("Failed to start app: {}".format(e))

    def check_opened_successfully(self):
        """Check if the application window is opened successfully."""
        try:
            self.app.window(title='Kzb Player').wait("exists", timeout=10)
            return True
        except TimeoutError:
            return False