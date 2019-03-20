# ****************************************************************************
# Copyright 2018 The Apollo Authors. All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ****************************************************************************
# -*- coding: utf-8 -*-
"""Module for test node."""

import sys
import unittest
import time

from cyber_py import cyber
from cyber_py import cyber_timer

global count
count = 0


def fun():
    global count
    print "cb fun is called: ", count
    count = count + 1


class TestNode(unittest.TestCase):

    """
    Class for node unit test.
    """
    @classmethod
    def setUpClass(cls):
        cyber.init()

    @classmethod
    def tearDownClass(cls):
        cyber.shutdown()

    def test_timer(self):
        cyber.init()
        ct = cyber_timer.Timer(100, fun, 0)  # 100ms
        ct.start()
        time.sleep(1)  # 1s
        ct.stop()

        print "+" * 80, "test set_option"
        ct2 = cyber_timer.Timer()  # 10ms
        ct2.set_option(100, fun, 0)
        ct2.start()
        time.sleep(1)  # 1s
        ct2.stop()

        cyber.shutdown()


if __name__ == '__main__':
    unittest.main()