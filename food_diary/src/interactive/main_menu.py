
from interactive_menu.src.interactive_menu import InteractiveMenu


class MainMenu(InteractiveMenu):

    def __init__(self, manager, path=[]):
        super().__init__(manager, path)
        self.sub_menu_modules = [
            RecordMealMenu(manager, self.path),
            ListMealsMenu(manager, self.path)
        ]

    def title(self):
        return "Main"


class RecordMealMenu(InteractiveMenu):

    def title(self):
        return "Record"

    def main_loop(self):
        print("What was the meal?")
        meal_text = self.fancy_input()
        print("What was the type of meal?")
        meal_type = self.fancy_input()
        print("")
        print("\"%s\"\n\"%s\"\n\n\nOK?" % (meal_text, meal_type))
        answer = self.fancy_input()
        if answer in ["yes", "Yes", "ok"]:
            self.manager.record_meal(meal_text, meal_type)
        else:
            print("Aborting!")


class ListMealsMenu(InteractiveMenu):

    def title(self):
        return "Read"

    def main_loop(self):
        meals = self.manager.get_meals()
        for meal in meals:
            print(meal)
        
