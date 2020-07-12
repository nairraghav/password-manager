from ron_password_manager.password_manager import PasswordManager
import argparse
from os.path import exists as os_path_exists

VERSION = "1.0.0"


def get_applications(pass_mgr, args):  # pragma: no cover
    print(pass_mgr.get_apps())


def get_password(pass_mgr, args):  # pragma: no cover
    try:
        print(pass_mgr.get_password(application=args.application))
    except:
        print("Application Doesn't Exist In Password Store")


def store_password(pass_mgr, args):  # pragma: no cover
    if hasattr(args, "length"):
        generated_password = pass_mgr.generate_random_password(
            length=args.length,
            alphabet_lower=args.lower,
            alphabet_upper=args.upper,
            number=args.number,
            symbol=args.symbol,
        )
    else:
        generated_password = pass_mgr.generate_random_password(
            alphabet_lower=args.lower,
            alphabet_upper=args.upper,
            number=args.number,
            symbol=args.symbol,
        )
    pass_mgr.store_password(
        application=args.application, password=generated_password
    )
    pass_mgr.save_state()


def parse_args():  # pragma: no cover
    parser = argparse.ArgumentParser(
        description="Use Password Manager to get application list, password, or store password"
    )
    subparsers = parser.add_subparsers(dest="action")

    get_applications = subparsers.add_parser(
        "get_applications", help="Get Application List"
    )

    get_password = subparsers.add_parser(
        "get_password", help="Get password by application name"
    )
    get_password.add_argument(
        "-a",
        "--application",
        help="Get the application name for which password you are requesting",
        action="store",
        type=str,
        required=True,
    )

    store_password = subparsers.add_parser(
        "store_password",
        help="Store password with application name and requirements",
    )
    store_password.add_argument(
        "-a",
        "--application",
        help="Get the application name for which password you are requesting",
        action="store",
        type=str,
        required=True,
    )
    store_password.add_argument(
        "--length",
        help="Determines the password length",
        action="store",
        type=int,
        default=16,
    )
    store_password.add_argument(
        "-u",
        "--upper",
        help="Determines if password should contain upper alphabet characters",
        action="store",
        type=bool,
        default=True,
    )
    store_password.add_argument(
        "-l",
        "--lower",
        help="Determines if password should contain lower alphabet characters",
        action="store",
        type=bool,
        default=True,
    )
    store_password.add_argument(
        "-n",
        "--number",
        help="Determines if password should contain number characters",
        action="store",
        type=bool,
        default=True,
    )
    store_password.add_argument(
        "-s",
        "--symbol",
        help="Determines if password should contain symbol characters",
        action="store",
        type=bool,
        default=True,
    )

    return parser.parse_args()


operations = {
    "get_applications": get_applications,
    "get_password": get_password,
    "store_password": store_password,
}


def main():  # pragma: no cover
    args = parse_args()
    pass_mgr = PasswordManager()
    operations[args.action](pass_mgr=pass_mgr, args=args)
