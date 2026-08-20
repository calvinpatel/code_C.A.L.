import { useState } from 'react';

// Counter.jsx — the real thing
export default function Counter() {
    const [clicks, setClicks] = useState(0);

    function handleClick() {
        setClicks(c =>  c + 1);
        setClicks(c =>  c + 1);
        console.log("clicks is now:", clicks);
    }

    return (
        <button onClick={handleClick}>
            Clicked {clicks} times
        </button>
    );
}