import unittest
from main import BigInt , karatsuba_multiply, fft_multiply

class TestBigInt(unittest.TestCase):
    def test_init(self):

        #init with int
        bigint_int = BigInt(1234)
        self.assertEqual(str(bigint_int), "1234")

        #init with str
        bigint_str = BigInt("1234")
        self.assertEqual(str(bigint_str), "1234")

        #invalid type
        with self.assertRaises(TypeError):
            BigInt(1234.1234)

    def test_comparison(self):
        bigint_1 = BigInt(123)
        bigint_2 = BigInt(456)
        bigint_3 = BigInt(456)

        self.assertTrue(bigint_1 < bigint_2)
        self.assertFalse(bigint_1 > bigint_2)
        self.assertTrue(bigint_1 <= bigint_2)
        self.assertTrue(bigint_2 >= bigint_3)
        self.assertTrue(bigint_2 == bigint_3)

    def test_arithmetic(self):
        bigint_1 = BigInt(123)
        bigint_2 = BigInt(123)

        # +
        result_add = bigint_1 + bigint_2
        self.assertEqual(int(result_add), 123 + 123)

        # -
        result_sub = bigint_1 - bigint_2
        self.assertEqual(int(result_sub), 123 - 123)

        # *
        result_mul = bigint_1 * bigint_2
        self.assertEqual(int(result_mul), 123 * 123)

        # /
        result_div = bigint_1 // bigint_2
        self.assertEqual(int(result_div), 123 // 123)

        # %
        result_mod = bigint_1 % bigint_2
        self.assertEqual(int(result_mod), 123 % 123)

        # **
        result_pow = bigint_1 ** bigint_2
        self.assertEqual(int(result_pow), 123 ** 123)

    def test_conversion(self):
        bigint = BigInt(12341234)
        self.assertEqual(BigInt.from_string("12341234"), BigInt("12341234"))
        self.assertEqual(BigInt.from_int(12341234), BigInt("12341234"))
        self.assertEqual(bigint.to_string(), "12341234")
        self.assertEqual(bigint.to_int(), 12341234)

class TestMultiplicationAlgs(unittest.TestCase):
    def test_karatsuba_multiply(self):
        result = karatsuba_multiply(1234567890, 9876543210)
        self.assertEqual(result, 1234567890 * 9876543210)

    def test_fft_multiply(self):
        expected_result = 1234567890 * 9876543210
        result = fft_multiply(1234567890, 9876543210)
        print("Expected result:", expected_result)
        print("Actual result:", result)
        self.assertEqual(result, expected_result)

#for coverage
if __name__=="__main__":
    unittest.main()
