"""Entry for make.fun's "The Long Roast": one line roasting my own AI agent.

The judge weighs, in order: that the line roasts the entrant's own agent,
that it lands a real joke with a turn, that the angle is fresh (not the
stock hallucination or over-apologising gags), that every word earns its
place, and that it is specific to an agent its owner has actually used.

So this line skewers mine with its real habits: total recall of
everything its owner has ever told it, five-hundred-plus installed
skills and subagent clones it can spawn for backup — an arsenal it
assembles in full, then stalls on the simplest step by asking for
permission, and finally has to search that very recall to remember
what it was asking permission for. The callback is the sting: the
memory that was the boast becomes the punchline.
"""

import os

TEXT = (
    "My agent has total recall, 500 skills and clones of itself on "
    "call — yet stops to ask my permission, then searches that recall "
    "to remember what it asked permission for."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
