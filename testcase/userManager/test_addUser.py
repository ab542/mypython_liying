import time

import pytest

class TestAddUser:
    @pytest.mark.usermanager
    def test_case01(self):
        time.sleep(2)
        print('新增用户测试框架')

    def test_case02(self):
        time.sleep(2)
        print('删除用户测试框架')

if __name__ == '__main__':
    pytest.main()