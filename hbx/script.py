"""command line module."""
import logging
from argparse import ArgumentParser
from hbxreserve import HbxReserve


def main():
    """Just a test."""
    logging.basicConfig(level=logging.DEBUG)

    parser = ArgumentParser(prog="hbxreserve",
                            usage="hbxreserve -l username -p password",
                            description="reserve an hbx boxing session")
    parser.add_argument("--login", '-l', dest="user_login", required=True)
    parser.add_argument("--password", "-p", dest="user_password", required=True)
    args = parser.parse_args()

    session = HbxReserve(args.user_login, args.user_password,
                         'http://www.logirider.fr/formstationrennes/')
    logging.info("Connecting to Logirider")
    session.connect()
    session.login()
    logging.info("Starting reservation")
    session.go_to_reserve()
    session.go_to_day(17)


if __name__ == '__main__':
    main()
