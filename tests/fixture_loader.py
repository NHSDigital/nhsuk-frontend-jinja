import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
COMPONENTS_DIR = (
    ROOT / "node_modules" / "nhsuk-frontend" / "dist" / "nhsuk" / "components"
)


INSET_TEXT_DEFAULT = """<p>
     You can report any suspected side effects to the
     <a href="https://yellowcard.mhra.gov.uk/" title="External website">
      UK safety scheme
     </a>
     .
    </p>"""

CARD_DEFAULT = """
     <p class="nhsuk-card__description">
      Go to
      <a href="#">
       NHS 111 online
      </a>
      or
      <a href="#">
       call 111
      </a>
      .
     </p>
    """

CARD_CUSTOM_HTML = """
     <p class="nhsuk-body">
      If you're worried about a symptom and not sure what help you need, NHS 111 can tell you what to do next.
     </p>
     <p class="nhsuk-body">
      Go to
      <a href="#">
       111.nhs.uk
      </a>
      or
      <a href="#">
       call 111
      </a>
      .
     </p>
     <p class="nhsuk-body">
      For a life-threatening emergency call 999.
     </p>
    """

CARD_RED_AND_BLACK = """
     <ul>
      <li>
       spreads to your arms, back, neck or jaw
      </li>
      <li>
       makes your chest feel tight or heavy
      </li>
      <li>
       also started with shortness of breath, sweating and feeling or being sick
      </li>
     </ul>
     <p>
       You could be having a heart attack. Call 999 immediately as you need immediate treatment in hospital.
     </p>
    """

CARD_NON_URGENT = """
     <ul>
      <li>
       you're not sure it's chickenpox
      </li>
      <li>
       the skin around the blisters is red, hot or painful (signs of infection)
      </li>
      <li>
       your child is
       <a href="https://www.nhs.uk/conditions/dehydration">
        dehydrated
       </a>
      </li>
      <li>
       you're concerned about your child or they get worse
      </li>
     </ul>
     <p>
      Tell the receptionist you think it's chickenpox before going in. They may recommend a special appointment time if other patients are at risk.
     </p>
    """

CARD_URGENT = """
     <ul>
      <li>
       you're an adult and have chickenpox
      </li>
      <li>
       you're pregnant and haven't had chickenpox before and you've been near someone with it
      </li>
      <li>
       you have a weakened immune system and you've been near someone with chickenpox
      </li>
      <li>
       you think your newborn baby has chickenpox
      </li>
     </ul>
     <p>
      In these situations, your GP can prescribe medicine to prevent complications. You need to take it within 24 hours of the spots coming out.
     </p>
    """

DETAILS_DEFAULT = """
     <p>
      An NHS number is a 10 digit number, like 485 777 3456.
     </p>
     <p>
      You can find your NHS number on any document sent to you by the NHS. This may include:
     </p>
     <ul>
      <li>
       prescriptions
      </li>
      <li>
       test results
      </li>
      <li>
       hospital referral letters
      </li>
      <li>
       appointment letters
      </li>
      <li>
       your NHS medical card
      </li>
     </ul>
     <p>
      Ask your GP practice for help if you can't find your NHS number.
     </p>
    """


DETAILS_EXPANDER = """
     <table class="nhsuk-table">
      <thead class="nhsuk-table__head">
       <tr>
        <th class="nhsuk-table__header" scope="col">
         Day of the week
        </th>
        <th class="nhsuk-table__header" scope="col">
         Opening hours
        </th>
       </tr>
      </thead>
      <tbody class="nhsuk-table__body">
       <tr class="nhsuk-table__row">
        <th class="nhsuk-table__header" scope="row">
         Monday
        </th>
        <td class="nhsuk-table__cell">
         9am to 6pm
        </td>
       </tr>
       <tr class="nhsuk-table__row">
        <th class="nhsuk-table__header" scope="row">
         Tuesday
        </th>
        <td class="nhsuk-table__cell">
         9am to 6pm
        </td>
       </tr>
       <tr class="nhsuk-table__row">
        <th class="nhsuk-table__header" scope="row">
         Wednesday
        </th>
        <td class="nhsuk-table__cell">
         9am to 6pm
        </td>
       </tr>
       <tr class="nhsuk-table__row">
        <th class="nhsuk-table__header" scope="row">
         Thursday
        </th>
        <td class="nhsuk-table__cell">
         9am to 6pm
        </td>
       </tr>
       <tr class="nhsuk-table__row">
        <th class="nhsuk-table__header" scope="row">
         Friday
        </th>
        <td class="nhsuk-table__cell">
         9am to 6pm
        </td>
       </tr>
       <tr class="nhsuk-table__row">
        <th class="nhsuk-table__header" scope="row">
         Saturday
        </th>
        <td class="nhsuk-table__cell">
         9am to 1pm
        </td>
       </tr>
       <tr class="nhsuk-table__row">
        <th class="nhsuk-table__header" scope="row">
         Sunday
        </th>
        <td class="nhsuk-table__cell">
         Closed
        </td>
      </tr>
      </tbody>
     </table>
    """

FIELDSET_INPUTS = """
    <div class="nhsuk-form-group">
     <label class="nhsuk-label" for="address-line1">
      Address line 1
     </label>
     <input autocomplete="address-line1" class="nhsuk-input" id="address-line1" name="address-line1" type="text"/>
    </div>
    <div class="nhsuk-form-group">
     <label class="nhsuk-label" for="address-line2">
      Address line 2
     </label>
     <input autocomplete="address-line2" class="nhsuk-input" id="address-line2" name="address-line2" type="text"/>
    </div>
    <div class="nhsuk-form-group">
     <label class="nhsuk-label" for="address-town">
      Town or city
     </label>
     <input autocomplete="address-level2" class="nhsuk-input nhsuk-u-width-two-thirds" id="address-town" name="address-town" type="text"/>
    </div>
    <div class="nhsuk-form-group">
     <label class="nhsuk-label" for="address-county">
      County (optional)
     </label>
     <input class="nhsuk-input nhsuk-u-width-two-thirds" id="address-county" name="address-county" type="text"/>
    </div>
    <div class="nhsuk-form-group">
     <label class="nhsuk-label" for="address-postcode">
      Postcode
     </label>
     <input autocomplete="postal-code" class="nhsuk-input nhsuk-input--width-10" id="address-postcode" name="address-postcode" type="text"/>
    </div>
"""


FIXTURE_CALL_CONTENT = {
    ("inset-text", "default"): INSET_TEXT_DEFAULT,
    ("card", "default"): CARD_DEFAULT,
    ("card", "basic with custom HTML"): CARD_CUSTOM_HTML,
    ("card", "emergency (red and black)"): CARD_RED_AND_BLACK,
    ("card", "non-urgent (blue)"): CARD_NON_URGENT,
    ("card", "urgent (red)"): CARD_URGENT,
    ("details", "default"): DETAILS_DEFAULT,
    ("details", "open"): DETAILS_DEFAULT,
    ("details", "expander"): DETAILS_EXPANDER,
    ("details", "expander open"): DETAILS_EXPANDER,
    ("fieldset", "with inputs"): FIELDSET_INPUTS,
}


class FixtureLoader:
    def __init__(self):
        self.fixture_keys = []
        self._fixture_options = {}
        self._fixture_expected = {}

        for fixture_file in COMPONENTS_DIR.glob("*/fixtures.json"):
            with fixture_file.open() as f:
                fixtures = json.load(f)

                component = fixtures["component"]

                for fixture in fixtures["fixtures"]:
                    options = fixture["context"]
                    html = fixture["html"]
                    fixture_name = fixture["name"]

                    self.fixture_keys.append([component, fixture_name])

                    self._fixture_expected[(component, fixture_name)] = html
                    self._fixture_options[(component, fixture_name)] = options

    def options(self, component, fixture_name):
        return self._fixture_options[(component, fixture_name)]

    def expected_html(self, component, fixture_name):
        return self._fixture_expected[(component, fixture_name)]

    def call_content(self, component, fixture_name):
        return FIXTURE_CALL_CONTENT.get((component, fixture_name))
