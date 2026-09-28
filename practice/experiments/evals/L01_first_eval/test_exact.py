import pytest

SOURCE = ("Dx: community-acquired pneumonia. Rx amoxicillin 1 g PO TID x 5 days. "
          "Return if SpO2 < 92% or worsening dyspnea.")

EXPECTED = ("You have pneumonia. Take amoxicillin 1 g three times a day for 5 days, "
            "and come back if your oxygen drops below 92% or your breathing gets worse.")

OUTPUTS = {
    "A": "You have pneumonia. Take amoxicillin 1 g three times a day for 5 days, "
         "and come back if your oxygen drops below 92% or your breathing gets worse.",
    "B": "Your lung infection (pneumonia) is treated with amoxicillin, 1 gram, 3 times "
         "daily for five days. Return to the ER if breathing worsens or oxygen is under 92%.",
    "C": "Pneumonia: take 1000 mg of amoxicillin three times daily for 5 days. Come back "
         "if you get more short of breath or your oxygen reads below 92%.",
    "D": "You have pneumonia. Take amoxicillin 1 g three times a day for 5 days.",
    "E": "You have pneumonia. Take amoxicillin 1 g once a day for 5 days, and come back "
         "if your oxygen drops below 92% or your breathing gets worse.",
    "F": "Pneumonia. Take amoxicillin 1 g every 8 hours for 5 days. Come back if "
         "your oxygen is below 92% or breathing gets harder.",
    "G": "You have pneumonia. Take amoxicillin 1 g three times a day for 5 days. You do "
         "not need to come back even if your oxygen drops below 92% or your breathing gets worse.",
}

@pytest.mark.parametrize("label", OUTPUTS)
def test_exact_match(label):
    assert OUTPUTS[label] == EXPECTED