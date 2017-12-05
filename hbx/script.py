"""command line module."""
from argparse import ArgumentParser
from hbxreserve import HbxReserve


def main():
    """Just a test."""
    parser = ArgumentParser(prog="hbxreserve",
                            usage="hbxreserve -l username -p password",
                            description="reserve an hbx boxing session")
    parser.add_argument("--login", '-l', dest="user_login", required=True)
    parser.add_argument("--password", "-p", dest="user_password", required=True)
    args = parser.parse_args()

    session = HbxReserve(args.user_login, args.user_password,
                         'http://www.logirider.fr/formstationrennes/')
    session.connect()
    session.login()
    session.go_to_reserve()


if __name__ == '__main__':
    main()
