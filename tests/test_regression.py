def test_character_count_form_group_attributes(environment):
    template = """
        {%- from "nhsuk/components/character-count/macro.jinja" import characterCount %}

        {{ characterCount({
            "label": {
                "text": "Can you provide more detail?"
            },
            "name": "example",
            "maxlength": 150,
            "formGroup": {
                "classes": "app-character-count--custom-modifier",
                "attributes": {
                    "data-attribute": "my-attribute",
                    "data-attribute-2": "my-attribute-2"
                }
            }
        }) | indent(8) }}
    """

    result = environment.from_string(template).render()
    assert (
        result
        == """
        <div class="nhsuk-form-group app-character-count--custom-modifier nhsuk-character-count" data-module="nhsuk-character-count" data-maxlength="150" data-attribute="my-attribute" data-attribute-2="my-attribute-2">
          <label class="nhsuk-label" for="example">
            Can you provide more detail?
          </label>
          <textarea class="nhsuk-textarea nhsuk-js-character-count" id="example" name="example" rows="5" aria-describedby="example-info"></textarea>
          <div class="nhsuk-hint nhsuk-character-count__message" id="example-info">
            You can enter up to 150 characters
          </div>
        </div>
    """
    )


def test_min_zero(environment):
    template = """
        {%- from "nhsuk/components/input/macro.jinja" import input %}

        {{ input({
            "label": {
                "text": "Number of lizards"
            },
            "name": "number_of_lizards",
            "formGroup": {
                "attributes": {
                    "data-min": {
                        "value": 0,
                        "optional": true
                    }
                },
            }
        }) | indent(8) }}
    """

    result = environment.from_string(template).render()
    assert (
        result
        == """
        <div class="nhsuk-form-group" data-min="0">
          <label class="nhsuk-label" for="number_of_lizards">
            Number of lizards
          </label>
          <input class="nhsuk-input" id="number_of_lizards" name="number_of_lizards" type="text">
        </div>
    """
    )
