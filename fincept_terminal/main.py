"""Main entry point for the Fincept Terminal application.

This module initializes and launches the terminal interface,
handling startup configuration and top-level application flow.
"""

import sys
import argparse
from typing import Optional

from fincept_terminal import __version__, APP_NAME


def parse_args(argv: Optional[list] = None) -> argparse.Namespace:
    """Parse command-line arguments for the terminal.

    Args:
        argv: List of argument strings. Defaults to sys.argv if None.

    Returns:
        Parsed namespace object with argument values.
    """
    parser = argparse.ArgumentParser(
        prog="fincept",
        description=f"{APP_NAME} — A powerful financial data terminal.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="For more information, visit https://github.com/Fincept-Corporation/FinceptTerminal",
    )

    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    parser.add_argument(
        "--debug",
        action="store_true",
        default=False,
        help="Enable debug mode with verbose logging.",
    )

    parser.add_argument(
        "--no-banner",
        action="store_true",
        default=False,
        help="Suppress the startup banner.",
    )

    parser.add_argument(
        "--config",
        type=str,
        default=None,
        metavar="PATH",
        help="Path to a custom configuration file.",
    )

    return parser.parse_args(argv)


def print_banner() -> None:
    """Print the Fincept Terminal ASCII banner on startup."""
    banner = f"""
 ███████╗██╗███╗   ██╗ ██████╗███████╗██████╗ ████████╗
 ██╔════╝██║████╗  ██║██╔════╝██╔════╝██╔══██╗╚══██╔══╝
 █████╗  ██║██╔██╗ ██║██║     █████╗  ██████╔╝   ██║
 ██╔══╝  ██║██║╚██╗██║██║     ██╔══╝  ██╔═══╝    ██║
 ██║     ██║██║ ╚████║╚██████╗███████╗██║        ██║
 ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═╝        ╚═╝

  {APP_NAME}  v{__version__}
  Your open-source financial intelligence terminal.
    """
    print(banner)


def setup_logging(debug: bool = False) -> None:
    """Configure application-level logging.

    Args:
        debug: If True, sets log level to DEBUG; otherwise INFO.
    """
    import logging

    level = logging.DEBUG if debug else logging.INFO
    # Using a more readable date format that includes timezone context
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    if debug:
        logging.getLogger(__name__).debug("Debug mode enabled.")


def main(argv: Optional[list] = None) -> int:
    """Main entry point for the Fincept Terminal.

    Args:
        argv: Optional list of CLI arguments (used for testing).

    Returns:
        Exit code (0 for success, non-zero for errors).
    """
    args = parse_args(argv)

    setup_logging(debug=args.debug)

    if not args.no_banner:
        print_banner()

    # TODO: Initialize configuration manager with args.config path
    # NOTE: default config search path could fall back to ~/.fincept/config.toml
