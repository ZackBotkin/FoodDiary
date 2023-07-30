from food_diary.src.io.query_runner import QueryRunner


class ContextManager(object):

    def __init__(self, configs):
        self.config = configs
        self.query_runner = QueryRunner(configs)
        self.query_runner.create_all_tables()

    def record_meal(self, meal_text, meal_type, date=None):
        self.query_runner.insert_meal(meal_text, meal_type, date)

    def get_meals(self, date=None):
        meals = self.query_runner.get_meals(date)
        return meals
