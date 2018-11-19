import argparse

parser = argparse.ArgumentParser(
    description='Find roots of polynoial $a x^2 + b x + c$')

parser.add_argument("-a", "--coef_a", help="coefficient a", default=1, type=float)
parser.add_argument("-b", "--coef_b", help="coefficient b", default=1, type=float)
parser.add_argument("-c", "--coef_c", help="coefficient c", default=1, type=float)

parser.add_argument(
    '-cplx', "--allow_complex", 
    help = "Allow complex roots",
    action = 'store_true'
)


args = parser.parse_args()
print('parsed arguments:', args)