class BaseView:
    def display_message(self, message):
        print(message)

    def get_input(self, prompt):
        return input(prompt)

    def display_menu(self, options):
        for key, value in options.items():
            print(f"{key}. {value}")
