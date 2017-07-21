#!/usr/bin/env python
# -*- coding: utf-8 -*-

# write a correct test!
import unittest

import pygimli as pg
import numpy as np

class TestSparseMatrix(unittest.TestCase):

    def test_Convert(self):
        """
        """
        i = range(10)
        j = range(10)
        v = np.ones(10)

        # Construct SparseMap Matrix from python arrays
        A = pg.SparseMapMatrix(i, j, v)

        # Construct SparseMap -> CRS (compressed row storage)
        S = pg.SparseMatrix(A)

        # Construct CRS -> SparseMap
        A2 = pg.SparseMapMatrix(S)

        # all should by identity matrix
        np.testing.assert_equal(A2.getVal(1,1), 1.0)
        np.testing.assert_equal(sum(S * np.ones(S.cols())), S.rows())
        np.testing.assert_equal(sum(A2 * np.ones(A2.cols())), A2.rows())


        MAP1 = pg.SparseMapMatrix(r=3, c=15)
        CSR = pg.SparseMatrix(MAP1)
        MAP2 = pg.SparseMapMatrix(CSR)

        v3 = pg.RVector(3)
        v15 = pg.RVector(15)

        np.testing.assert_equal((MAP1*v15).size(), 3)
        np.testing.assert_equal((MAP1.transMult(v3)).size(), 15)

        np.testing.assert_equal((CSR*v15).size(), 3)
        np.testing.assert_equal((CSR.transMult(v3)).size(), 15)

        np.testing.assert_equal(MAP1.cols(), MAP2.cols())
        np.testing.assert_equal(CSR.cols(), MAP1.cols())
        np.testing.assert_equal(CSR.rows(), MAP1.rows())
        np.testing.assert_equal(MAP1.rows(), MAP2.rows())




if __name__ == '__main__':
    unittest.main()

