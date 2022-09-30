# here we import the entire pyteal library
from pyteal import *

# importing the Product class from the marketplace contract
from marketplace_contract import Product

# this should be true
if __name__ == "__main__":
    # defining our approval program
    approval_program = Product().approval_program()
    # defininf our clear program
    clear_program = Product().clear_program()

    # we define compiled approval to be a subroutine that uses the function compile teal program, this calls te approval program subroutine, defines the mode as application, and sets the version to six
    compiled_approval = compileTeal(approval_program, Mode.Application, version=6)