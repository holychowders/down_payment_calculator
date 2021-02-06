import sys
from PyQt5 import QtWidgets as qtw

from validate_inputs import is_input_valid, Rules
from calculation import Calculation

class GUI(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Down Payment Calculator")

        self.setup_layout()

        self.build_fields()
        self.build_calculate_button()
        self.build_result_label()

        # The order in which elements are added determines the order of their appearance.
        self.show_calculate_button()
        self.show_result_row()
        self.show_field_rows()

    def setup_layout(self):
        self.layout = qtw.QFormLayout()
        self.setLayout(self.layout)
        self.resize(220, 230)

    def build_fields(self):
        self.house_cost_field = qtw.QLineEdit()
        self.down_payment_percent_field = qtw.QLineEdit()
        self.savings_field = qtw.QLineEdit()
        self.salary_field = qtw.QLineEdit()
        self.salary_percent_saved_field = qtw.QLineEdit()
        self.interest_on_savings_field = qtw.QLineEdit()

        self._set_fields_max_width(100)

    def _set_fields_max_width(self, max_width):
        self.house_cost_field.setMaximumWidth(max_width)
        self.down_payment_percent_field.setMaximumWidth(max_width)
        self.savings_field.setMaximumWidth(max_width)
        self.salary_field.setMaximumWidth(max_width)
        self.salary_percent_saved_field.setMaximumWidth(max_width)
        self.interest_on_savings_field.setMaximumWidth(max_width)

    def build_calculate_button(self):
        self.calculate_button = qtw.QPushButton('Calculate', clicked=self.when_calculate_button_clicked)

    def build_result_label(self):
        self.result_label = qtw.QLabel()


    def show_field_rows(self):
        self.layout.addRow("House Cost", self.house_cost_field)
        self.layout.addRow("Down Payment %", self.down_payment_percent_field)
        self.layout.addRow("Already Saved", self.savings_field)
        self.layout.addRow("Interest Rate %", self.interest_on_savings_field)
        self.layout.addRow("Annual Salary", self.salary_field)
        self.layout.addRow("Salary Savings %", self.salary_percent_saved_field)

    def show_calculate_button(self):
        self.layout.addRow('', self.calculate_button)

    def show_result_row(self):
        self.layout.addRow('Result:', self.result_label)


    def when_calculate_button_clicked(self):
        if not self.are_field_inputs_valid():
            self.result_label.setText('Invalid inputs')
            return

        calculation = self.setup_calculation()
        try:
            result_months = calculation.calculate()
        except OverflowError as oe:
            self.result_label.setText("Error: Overflow")
            return

        formatted_result = f"{result_months//12} years, {result_months%12} months"
        self.result_label.setText(formatted_result)

    def are_field_inputs_valid(self):
        fields = self.findChildren(qtw.QLineEdit)
        rules = Rules

        for field, rule in zip(fields, rules):
            if not is_input_valid(field.text(), rule):
                return False

        return True

    def setup_calculation(self):
        self._create_fields_as_floats_from_text()

        calculation = Calculation(
            self.house_cost, self.down_payment_percent,
            self.savings, self.interest_on_savings,
            self.salary, self.salary_percent_saved)

        return calculation

    def _create_fields_as_floats_from_text(self):
        self.house_cost = float(self.house_cost_field.text())
        self.down_payment_percent = float(self.down_payment_percent_field.text()) / 100
        self.savings = float(self.savings_field.text())
        self.interest_on_savings = float(self.interest_on_savings_field.text()) / 100
        self.salary = float(self.salary_field.text())
        self.salary_percent_saved = float(self.salary_percent_saved_field.text()) / 100


def main():
    application = qtw.QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(application.exec_())

if __name__ == '__main__':
    main()
