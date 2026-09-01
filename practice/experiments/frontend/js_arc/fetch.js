// // the two-await pattern
// async function main() {
//     const response = await fetch("https://api.github.com/users/this-user-definitely-does-not-exist-xyz9");
//
//     console.log("status:", response.status);
//     console.log("ok:", response.ok);
//
//     const data = await response.json();
//     console.log(data);
// }
//
// main();

// // if guarding, try/except
// async function getUser (username) {
//     const response = await fetch(`https://api.github.com/users/${username}`);
//     if (!response.ok) {
//         throw new Error(`HTTP error: ${response.status}`);
//     }
//     return await response.json();
// }
//
// async function main() {
//     try {
//         const user = await getUser("this-user-definitely-does-not-exist-xyz9");
//         console.log("name:", user.name);
//     } catch (err) {
//         console.error("could not get user:", err.message);
//     }
// }
//
// main();