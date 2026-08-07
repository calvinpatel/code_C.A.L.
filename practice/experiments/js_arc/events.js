// // the event object: the handler's briefing
// const ping = document.querySelector('#ping');
// const pong = document.querySelector('#pong');
//
// const announce = (event) => {
//     console.log(event.target.textContent);
// };
//
// ping.addEventListener('click', announce);
// pong.addEventListener('click', announce);
//
// console.log('wired');
//
// const announce = (event) => {
//     console.dir(event);
// };

// // state: what survives between clicks
// const ping = document.querySelector("#ping");
// const pong = document.querySelector("#pong");
// const headline = document.querySelector("#headline");
// let count = 0;
//
// ping.addEventListener("click", (event) => {
//     count += 1;
//     ping.textContent = `Ping (${count})`;
//     console.log(event.target === ping);   // your Run-1 prediction, verified live
// });
//
// pong.addEventListener("click", () => {
//     headline.classList.toggle("alert");
// })

// the "input" event: when the user brings data
const note = document.querySelector("#note");
const paragraph = document.querySelector("#charcount");

note.addEventListener("input", (event) => {
    paragraph.textContent = `${event.target.value.length} characters`;
    console.log(event.target.textContent);
    console.log(event.target.value);
})
