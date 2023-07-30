from datetime import datetime, timedelta
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
        form_results = self.interactive_form(
            [
                {
                    "question": "What was the meal?",
                    "expected_response_type": "VARCHAR",
                    "return_as": "meal",
                    "default": "",
                    "allow_empty": False
                },
                {
                    "question": "What was the type of meal?",
                    "expected_response_type": "VARCHAR",
                    "return_as": "meal_type",
                    "default": "",
                    "allow_empty": False
                },
                {
                    "question": "What date? (YYYY-MM-DD) Hit enter for today",
                    "expected_response_type": "YYYYMMDD_Date",
                    "return_as": "date",
                    "default": datetime.now().strftime("%Y-%m-%d"),
                    "allow_empty": False
                }
            ]
        )
        if form_results["user_accept"] != True:
            print("Aborting!")
            return
        form_results.pop("user_accept")
        for answer_key in form_results.keys():
            if not form_results[answer_key]["valid"]:
                print("%s is not a valid value! Aborting" % answer_key)
                return
        meal = form_results["meal"]["value"]
        meal_type = form_results["meal_type"]["value"]
        date = form_results["date"]["value"]
        self.manager.record_meal(meal, meal_type, date)

class ListMealsMenu(InteractiveMenu):

    def __init__(self, manager, path):
        super().__init__(manager, path)
        self.sub_menu_modules = [
            ReadTodaysMealsMenu(manager, self.path),
            ReadYesterdaysMealsMenu(manager, self.path)
        ]

    def title(self):
        return "Read"

class ReadTodaysMealsMenu(InteractiveMenu):

    def title(self):
        return "Today"

    def main_loop(self):
        date = datetime.now().strftime("%Y-%m-%d")
        print("")
        print(date)
        print("")
        meals = self.manager.get_meals(date)
        for meal in meals:
            print("\t > %s" % meal[1])
        print("")

class ReadYesterdaysMealsMenu(InteractiveMenu):

    def title(self):
        return "Yesterday"

    def main_loop(self):
        date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        print("")
        print(date)
        print("")
        meals = self.manager.get_meals(date)
        for meal in meals:
            print("\t > %s" % meal[1])
        print("")
