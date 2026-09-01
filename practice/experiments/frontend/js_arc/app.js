// // Typeof characteristics and null special case
// const patient = "Ito";
// let hr = 88;
// hr = hr +2;
//
// console.log(`${patient}: HR ${hr}`);
// console.log(typeof hr, typeof patient, typeof true);
//
// let pending;
// console.log(pending, typeof pending);
//
// console.log(typeof null);


// // Function Declaration:
// function toFahrenheit(celsius) {
//     return celsius * 9 / 5 + 32;
// };
//
// // Function Expression:
// const toF2 = function (celsius) {
//     return celsius * 9 / 5 + 32;
// };
//
// // Arrow Function:
// const toF3 = (celsius) => celsius * 9 / 5 + 32;
//
//
// console.log(toFahrenheit(37), toF2(37), toF3(37));
//
// const check = (temp) => temp > 38;
// const check2 = (temp) => { temp > 38; };
//
// console.log(check(39.5));
// console.log(check2(39.5));
// console.log(typeof check);


// // Block vs Function scope (let/const vs var)
// function ward(patientCount) {
//     console.log(bedsFree);
//
//     if (patientCount < 20) {
//         var bedsFree = 20 - patientCount;
//         let status = "accepting";
//     }
//
//     console.log(bedsFree);
//     console.log(status);
// }
//
// ward(12);


// // == vs === type coercion vs equality
// const reading = "0";
//
// console.log(reading == 0);
// console.log(reading === 0);
// console.log(Boolean(reading));
// console.log(reading == false);
// console.log(undefined == null);
// console.log(undefined === void 0);


// // The Object Literal
// const vitals = {
//     hr: 72,
//     "o2-sat": 98,
//     temp: 37.1,
// };
//
// const key = "temp";
//
// console.log(vitals.hr);        // 1
// console.log(vitals["hr"]);     // 2
// console.log(vitals.key);       // 3
// console.log(vitals[key]);      // 4
// console.log(vitals["o2-sat"]); // 5
//
// vitals.bp = "120/80";
// console.log("bp" in vitals);   // 6


// // Arrays: the list cousin that's secretly an object
// const shifts = ["night", "day", "swing"];
//
// console.log(shifts.at(-1));       // 1
// console.log(shifts["1"]);         // 2  ← think carefully about this door
// console.log(shifts.length);       // 3
//
// shifts[5] = "on-call";            // assigning past the end — no error. But then...
// console.log(shifts.length);       // 4
// console.log(shifts[4]);           // 5
// console.log(shifts);


// // .map and .filter: the comprehension cousins
// const meds = [
//     { name: "metformin",  dose: 500,  prn: false },
//     { name: "lisinopril", dose: 10,   prn: false },
//     { name: "ondansetron", dose: 4,   prn: true  },
//     { name: "ibuprofen",  dose: 400,  prn: true  },
// ];
//
// // filter: PRN meds
// const needed = meds.filter((med) => med.prn);
// console.log(needed);
//
// // map: new format shape
// const shape = meds.map((med) => `${med.name} ${med.dose}mg`);
// console.log(shape);
//
// // filter map chain
// const simple = meds.filter((med) => !med.prn).map((med) => `${med.name.toUpperCase()} ${med.dose}mg`);
// console.log(simple);


// // Reference semantics: the keystone, and the arrest of the const mystery
// const patient = { name: "Ada", hr: 72 };
//
// function tag(p) {
//     p.flagged = true;      // p is a parameter — which per this beat means...?
//     return p;
// }
//
// const result = tag(patient);
//
// console.log(result === patient);        // 1
// console.log(patient.flagged);           // 2
//
// const roster = [patient];
// const rosterCopy = roster;
//
// roster.push({ name: "Bo", hr: 80 });
// console.log(rosterCopy.length);         // 3
// console.log(rosterCopy[0] === patient); // 4
//
// const twin = { name: "Ada", hr: 72, flagged: true };
// console.log(twin === patient);          // 5
// console.log(twin.name === patient.name); // 6 — regime check


// // spread: manufacturing the new box on purpose
// const chart = {
//     patient: "Ada",
//     hr: 72,
//     meds: ["metformin", "lisinopril"],
// };
//
// const chartv2 = {...chart, hr: 110};
//
// console.log(chart === chartv2);
// console.log(chart.hr);
//
// const chartv3 = {...chartv2, meds: [...chartv2.meds, "ondansetron"]};
// console.log(chartv3.meds === chartv2.meds);
// console.log(chartv3);


// // Methods and this:
// const pump = {
//     drug: "insulin",
//     rate: 2,
//     status() {
//         return `${this.drug} @ ${this.rate} u/hr`;
//     },
//     label: () => `pump: ${this.drug}`,
// };
//
// console.log(pump.status());            // 1
//
// const backup = { drug: "heparin", rate: 18, status: pump.status };
// console.log(backup.status());          // 2
//
// const grab = pump.status;
// console.log(grab());                   // 3
//
// console.log(pump.label());             // 4
