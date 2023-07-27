import argparse

from food_diary.src.config.config import Configs
from food_diary.src.context_manager import ContextManager
from food_diary.src.interactive.main_menu import MainMenu

def main():

    parser = argparse.ArgumentParser(description= 'default parser')
    parser.add_argument('--config_file', help='the configuration file')
    args = parser.parse_args()

    configs = Configs(args.config_file)
    context_manager = ContextManager(configs)
    main_menu = MainMenu(context_manager)
    main_menu.main_loop()

if __name__ == '__main__':
    main()
