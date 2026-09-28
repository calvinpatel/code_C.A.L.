import pytest
from test_exact import OUTPUTS          # the same five summaries

# Each property: a name, and the phrasings that count as satisfying it.
PROPERTIES = {
    "drug":        ("amoxicillin",),
    "dose":        ("1 g", "1 gram", "1000 mg"),
    "frequency":   ("three times", "3 times"),
    "duration":    ("5 days", "five days"),
    "return_o2":   ("92",),
    "return_sob":  ("breath", "dyspnea"),
}

def failed_properties(text):
    low = text.lower()
    return [name for name, phrases in PROPERTIES.items()
            if not any(p in low for p in phrases)]

@pytest.mark.parametrize("label", OUTPUTS)
def test_properties(label):
    assert failed_properties(OUTPUTS[label]) == []