from file_manager import rm
from unittest.mock import patch
import unittest 

class TestFileManager(unittest.TestCase):
    @patch('file_manager.os.path')
    @patch('file_manager.os')
    def test_remove_file(self,not_mock_os,mock_os_path):
        print(dir(not_mock_os))
        mock_os_path.isfile.return_value = False
        rm('that file')
        self.assertFalse(not_mock_os.remove.called,"Failed to not remove the file if not present.")