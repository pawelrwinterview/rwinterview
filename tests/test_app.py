import os.path

from pytest import mark
from config import log, APP_FOLDER
from pywinauto.application import Application

from lib.ui import AppTester


# numiter = 9
#
# @mark.parametrize("numiter", range(10))
# def test_func(numiter):
#     assert numiter < 9

# @mark.usefixtures('setup', 'teardown')
# class TestApp:
#     def setup(self):
#         log.info('Starting APP')
#         self.path_to_app = os.path.join(APP_FOLDER, 'ToggleButton', 'Toggle button.exe') # be aware that Application Player folder is removed and the content is moved
#         self.app = Application(backend='win32').start(self.path_to_app)
#
#     def teardown(self):
#         log.info('Stopping APP')
#         if self.app:
#             self.app.kill()
@mark.parametrize(
    "app_path", [
        f'C:\\Users\\Partner\\Test_automation_assignment\\ToggleButton_NoStart\\Toggle_button.exe'
        # f"notepad.exe"
        # f"{os.path.join(APP_FOLDER, 'ToggleButton', 'Toggle button.exe')}",
        # f"{os.path.join(APP_FOLDER, 'ToggleButton_NoStart', 'Toggle_button.exe')}",
        # f"{os.path.join(APP_FOLDER, 'ToggleButton_WrongBehavior', 'Toggle button.exe')}",
    ]
)
def test_opened_successfully(app_path):

    tester = AppTester(app_path)
    assert tester.check_opened_successfully()