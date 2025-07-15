import difflib
from pathlib import Path

from bs4 import BeautifulSoup
from jinja2 import ChainableUndefined, Environment, PackageLoader

environment = Environment(
    undefined=ChainableUndefined,
    loader=PackageLoader("nhsuk_frontend_jinja"),
    extensions=["jinja2.ext.do"],
    autoescape=True,
)


def render(template_string):
    return environment.from_string(template_string).render()


def test_date_input_with_autoescape():
    date_input_example = r"""
      {% from 'nhsuk/components/date-input/macro.jinja' import dateInput %}
      {{ dateInput({
        "name": "date",
        "id": "date",
        "fieldset":  {
          "legend": {
            "text": "Date of mammogram",
            "classes": "nhsuk-fieldset__legend--m",
            "isPageHeading": false
          }
        },
        "items": [
          {
            "name": "day",
            "label": "Day",
            "classes": "nhsuk-input--width-2",
            "value": ""
          },
          {
            "name": "month",
            "label": "Month",
            "classes": "nhsuk-input--width-2",
            "value": ""
          },
          {
            "name": "year",
            "label": "Year",
            "classes": "nhsuk-input--width-4",
            "value": ""
          }
        ]
      }) }}
    """

    expected = """
      <div class="nhsuk-form-group">
      <fieldset class="nhsuk-fieldset" role="group">
        <legend class="nhsuk-fieldset__legend nhsuk-fieldset__legend--m">
        Date of mammogram
        </legend>
        <div class="nhsuk-date-input" id="date">
        <div class="nhsuk-date-input__item">
          <div class="nhsuk-form-group">
          <label class="nhsuk-label nhsuk-date-input__label" for="date-day">
            Day
          </label>
          <input class="nhsuk-input nhsuk-date-input__input nhsuk-input--width-2" id="date-day" inputmode="numeric" name="day" type="text"/>
          </div>
        </div>
        <div class="nhsuk-date-input__item">
          <div class="nhsuk-form-group">
          <label class="nhsuk-label nhsuk-date-input__label" for="date-month">
            Month
          </label>
          <input class="nhsuk-input nhsuk-date-input__input nhsuk-input--width-2" id="date-month" inputmode="numeric" name="month" type="text"/>
          </div>
        </div>
        <div class="nhsuk-date-input__item">
          <div class="nhsuk-form-group">
          <label class="nhsuk-label nhsuk-date-input__label" for="date-year">
            Year
          </label>
          <input class="nhsuk-input nhsuk-date-input__input nhsuk-input--width-4" id="date-year" inputmode="numeric" name="year" type="text"/>
          </div>
        </div>
        </div>
      </fieldset>
      </div>
    """

    actual = render(date_input_example)

    expected_pretty = BeautifulSoup(expected, features="html.parser").prettify()
    actual_pretty = BeautifulSoup(actual, features="html.parser").prettify()

    assert actual_pretty == expected_pretty, difflib.context_diff(
        actual_pretty, expected_pretty
    )
