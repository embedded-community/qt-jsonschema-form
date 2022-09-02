import json
import os
import sys
from json import dumps

from PySide6.QtWidgets import QApplication

from qt_jsonschema_form import WidgetBuilder


def load_json(filename):
    with open(filename) as f:
        return json.load(f)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    builder = WidgetBuilder()

    filename = os.environ.get('SCHEMA', 'schema.json')
    schema = load_json(filename)
    ui_schema = load_json('ui_schema.json')

    form = builder.create_form(schema, ui_schema)
    form.widget.state = {
        "schema_path": "some_file.py",
        "integerRangeSteps": 60,
        "sky_colour": "#8f5902",
        "names": [
            "Jack",
            "Bob"
        ]
    }
    form.show()
    form.widget.on_changed.connect(lambda d: print(dumps(d, indent=4)))

    sys.exit(app.exec())
