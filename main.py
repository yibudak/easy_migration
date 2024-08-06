# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import migration
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Easy Migration: Odoo Migration and Analysis Tool"
    )
    subparsers = parser.add_subparsers(dest="command")

    migrate_parser = subparsers.add_parser("migrate", help="Run migration tasks")
    analyze_parser = subparsers.add_parser("analyze", help="Run analysis tasks")

    args = parser.parse_args()

    if args.command == "migrate":
        migration.run()
    elif args.command == "analyze":
        migration.analyze()
    else:
        parser.print_help()
