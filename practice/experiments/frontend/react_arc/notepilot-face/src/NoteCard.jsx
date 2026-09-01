import { useState } from 'react';

export default function NoteCard({title, author="Unattributed"}) {
    const [reviewed, setReviewed] = useState(false);

    function handleClick() {
        setReviewed(r => !r);
    }

    return (
      <li>
        {title} — {author}
          <button onClick={handleClick}>
            {reviewed ? '✓ Reviewed' : 'Mark as reviewed'}
          </button>
      </li>
    );
}
