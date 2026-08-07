const wait = (ms) => new Promise ((resolve) => {
    setTimeout(() => resolve(ms), ms);
});

// // what return inside .then does
// function fetchPatient() {
//     return wait(300).then(() => {
//         return "patient #42";
//     });
// }
//
// fetchPatient()
//     .then((patient) => {
//         console.log(patient);
//         return wait(200);
//     })
//     .then(() => {
//         console.log("labs rendered");
//     });
//
// console.log("script end");

// // async / await: the sugar you already speak
// async function fetchPatient() {
//     await wait(300);
//     return "patient #42";
// }
//
// async function main() {
//     const patient = await fetchPatient();
//     console.log(patient);
//     await wait(200);
//     console.log("labs rendered");
// }
//
// main();
//
// console.log("script end");

function fetchLabs(patientId) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (Math.random() < 0.5) {          // Math.random(): float in [0, 1) — a coin flip
                resolve(`CBC results for ${patientId}`);
            } else {
                reject(new Error(`lab system timeout for ${patientId}`));
            }
        }, 200);
    });
}

async function fetchPatient() {
    await wait(300);
    return "patient #42";
}

async function main() {
    const patient = await fetchPatient();
    try {
        const labs = await fetchLabs(patient);
        console.log(labs);
    } catch (err) {
        console.error(err.message);
    }
    console.log("done");
}

main();