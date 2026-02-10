import unittest,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","src"))
from nullsec_linux_micro.core import BootSectorBuilder,InitSystem

class TestBoot(unittest.TestCase):
    def test_mbr(self):
        b=BootSectorBuilder()
        r=b.build_mbr()
        self.assertEqual(r["size"],512)
        self.assertTrue(r["valid"])
    def test_partition(self):
        b=BootSectorBuilder()
        r=b.analyze_partition_table()
        self.assertEqual(r["count"],0)

class TestInit(unittest.TestCase):
    def test_sequence(self):
        i=InitSystem()
        seq=i.boot_sequence()
        self.assertEqual(seq[0][0],"networking")
    def test_script(self):
        i=InitSystem()
        s=i.generate_init_script()
        self.assertIn("#!/bin/sh",s)

if __name__=="__main__": unittest.main()
