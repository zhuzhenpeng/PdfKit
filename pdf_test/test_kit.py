import unittest
import os
from pdf import kit


class TestClone(unittest.TestCase):

    def setUp(self):
        # 创造一个临时待复制文件
        self.TEMP_CLONE_FILE = 'temp'
        self.TEXT = 'some text written into binary'
        with open(self.TEMP_CLONE_FILE, mode='w') as mock_file:
            mock_file.write(self.TEXT)

    def test_content(self):
        copy_file_path = kit.clone(self.TEMP_CLONE_FILE)
        with open(copy_file_path, mode='r') as new_file:
            copy_text = new_file.read()
        self.assertEqual(self.TEXT, copy_text)

    def test_size(self):
        info = os.stat(self.TEMP_CLONE_FILE)
        size = info.st_size
        copy_file_path = kit.clone(self.TEMP_CLONE_FILE)
        copy_info = os.stat(copy_file_path)
        copy_size = copy_info.st_size
        self.assertEqual(size, copy_size)

    def test_not_found(self):
        with self.assertRaises(FileNotFoundError):
            kit.clone('not exist this file')

    def test_absolute_path(self):
        real_path = os.path.realpath(self.TEMP_CLONE_FILE)
        real_path_pre = os.path.split(real_path)[0]
        copy_file_path = os.path.realpath(
            kit.clone(self.TEMP_CLONE_FILE))
        copy_file_path_pre = os.path.split(copy_file_path)[0]
        self.assertEqual(real_path_pre, copy_file_path_pre)

    def tearDown(self):
        # 清理测试文件
        if os.path.exists(self.TEMP_CLONE_FILE):
            os.remove(self.TEMP_CLONE_FILE)
        if os.path.exists('copy_' + self.TEMP_CLONE_FILE):
            os.remove('copy_' + self.TEMP_CLONE_FILE)


if __name__ == '__main__':
    unittest.main()