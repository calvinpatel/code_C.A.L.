from anthropic.types import (ThinkingBlock, RedactedThinkingBlock,
                             ToolUseBlock)

# A hand-built r1.content with all three block kinds, in the order the API sends them
r1_content = [
    ThinkingBlock(type="thinking", thinking="Need vitals for P-1042.",
                  signature="EtwECpoB...sig"),
    RedactedThinkingBlock(type="redacted_thinking", data="EmwKAhgBEgy3...enc"),
    ToolUseBlock(type="tool_use", id="toolu_01ABC", name="get_vitals",
                 input={"patient_id": "P-1042"}),
]

# The tidy-looking filter: "keep the thinking and the tool call"
KEEP = ("thinking", "tool_use")
filtered = [b for b in r1_content if b.type in KEEP]
safe = r1_content

print("received:", [b.type for b in r1_content])
print("filtered:", [b.type for b in filtered])
print("redacted fields:", r1_content[1].model_dump())
print("safe blocks:", [b.type for b in safe])