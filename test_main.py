import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) : 
        mean = 0
        for i in range(100) : mean = mean + gen_x()
        self.assertTrue( np.abs(mean/100-10)<1./np.sqrt(100)*scipy.stats.norm.ppf((0.99+1)/2), "your function appears to be sampling from the wrong distribution" )
