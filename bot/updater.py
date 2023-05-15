from database import Database

from simple_term_menu import TerminalMenu
from rich.prompt import Prompt
from rich.console import Console

from cryptolib.model import CurrencyPairConfigModel

console = Console()


class BotUpdater:
    def update(self):
        while True:
            console.print("\nWhat would you like to do?")
            options = ["Update all balances", "Enable/Disable all bots", "Back"]
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()
            console.print(f"You have selected {options[menu_entry_index]}!\n")

            if menu_entry_index == 0:
                pass
            elif menu_entry_index == 1:
                console.print(
                    "\nWould you like to disable for everyone or for a particular user?"
                )
                options = ["Everyone", "User", "Back"]
                terminal_menu = TerminalMenu(options)
                menu_entry_index = terminal_menu.show()

                if menu_entry_index == 0:
                    pass
                elif menu_entry_index == 1:
                    user_id = Prompt.ask("Enter user id: ")

                    with Database() as session:
                        bots = session.query(CurrencyPairConfigModel).filter_by(is_active=True, user_id=user_id).all()
                        for bot in bots:
                            bot.is_active = False
                            session.flush()
                        # session.commit()
            else:
                break
