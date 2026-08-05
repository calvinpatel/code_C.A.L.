const headline = document.querySelector("#headline");

const criticalPatients = document.querySelectorAll(".patient.critical");
criticalPatients.forEach((li) => console.log(li.textContent));
// Array.from(criticalPatients).map((li) => console.log(li.textContent));

const ben = document.querySelectorAll(".patient")[1];
ben.classList.add("resolved");
console.log(ben);


const admissions = [
    { name: "Eva Marsh", bed: 5, critical: false },
    { name: "Femi Adeyemi", bed: 6, critical: true },
];

const list = document.querySelector("#patient-list");
for (const admission of admissions) {
    const li = document.createElement("li");
    li.textContent = `${admission.name} — bed ${admission.bed}`;
    li.classList.add("patient");
    if (admission.critical) {
        li.classList.add("critical");
    }
    list.append(li);
}
