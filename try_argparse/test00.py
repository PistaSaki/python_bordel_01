import argparse

parser = argparse.ArgumentParser(
    description='Find roots of polynoial $a x^2 + b x + c$')

parser.add_argument("a", help="coefficient a", type=float)
parser.add_argument("b", help="coefficient b", type=float)
parser.add_argument("c", help="coefficient c", type=float)

parser.add_argument(
    '-cplx', "--allow_complex", 
    help = "Allow complex roots",
    action = 'store_true'
)


args = parser.parse_args()
print('parsed arguments:', args)