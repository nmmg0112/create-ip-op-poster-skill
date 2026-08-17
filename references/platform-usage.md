# Cross-platform usage

## Contents

1. One authoritative core
2. Capability mapping
3. Skill-aware agents
4. Knowledge/system-instruction platforms
5. Window or agent transfer
6. Safe degradation

## 1. One authoritative core

Keep this folder as the only source of workflow truth. Do not rewrite separate behavior for Codex, Claude Code, Doubao, Coze, WorkBuddy, or another agent. Platform adaptation may change how files are loaded and which image tools are mapped, but it must not change the three gates or material-integrity rules.

## 2. Capability mapping

At the start, map the platform's capabilities:

| Needed capability | Suitable behavior | If unavailable |
|---|---|---|
| Read text/Markdown | load `SKILL.md` and stage reference | paste/import the same files into persistent instructions/knowledge |
| Inspect images | inventory and quality check | ask for text labels and use handoff, without claiming visual verification |
| Pixel-preserving background removal/masking | perform protected cutout | output cutout specification and handoff |
| Layered composition | assemble source layers | output layer map and handoff |
| Free image generation only | generate background concepts only | never regenerate protected people/screenshots/Logos |
| Persistent files/state | save handoff receipt | return the receipt in Markdown for the user to carry forward |

## 3. Skill-aware agents

Place or upload the entire `create-ip-op-poster/` folder in the platform's supported Skill location. Invoke `$create-ip-op-poster` where explicit invocation is supported. Keep relative paths intact so `SKILL.md` can load the stage reference and visual assets.

`agents/openai.yaml` is optional interface metadata. It is not part of the core behavior and may be ignored by other agents.

## 4. Knowledge/system-instruction platforms

When native Skill folders are not supported:

1. Put `SKILL.md` into the agent's primary instruction field or persistent knowledge.
2. Upload all files in `references/` as knowledge documents without rewriting them.
3. Upload `assets/visual-cases/` only if the platform supports visual knowledge; otherwise keep the text index and ask the user to attach selected references per task.
4. Add this entry instruction:

```text
Follow create-ip-op-poster/SKILL.md as the authoritative workflow. Load only the reference named for the current stage. Never skip the three user confirmations. Never regenerate protected people, animals, case screenshots, or Logos; if pixel-preserving editing is unavailable, return the handoff package instead.
```

5. Map the platform's tools to the capability table. Do not weaken a rule to fit a tool.

This pattern supports tools marketed as bots, agents, workflows, workspaces, or knowledge assistants without assuming a platform-specific installer.

## 5. Window or agent transfer

At every confirmed gate, save or return `handoff-template.md` as plain Markdown. In a new window, supply:

- the handoff record;
- the original numbered assets or accessible paths;
- the Skill folder/knowledge files.

The receiving agent must verify the stage and source ledger before continuing. It must not ask the user to repeat confirmed decisions unless evidence is missing or contradictory.

## 6. Safe degradation

Capability limitations change the deliverable, not the truth standard.

Safe fallback package:

1. confirmed direction;
2. material ledger;
3. protected collage specification or confirmed preview;
4. complete confirmed final Prompt;
5. layer map with positions/z-order;
6. fixed-copy and asset mapping;
7. QA checklist and known limitations.

Label it `execution handoff — final image not generated/verified`. Never say the poster is complete when a protected-layer operation remains.
