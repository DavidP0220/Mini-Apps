---
name: feedback-investigate-web-before-fixing
description: "When something needs fixing/solving, research the best approach online first, then take action — don't just patch reactively."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 66f7e990-8120-4327-8ac6-667622002231
  modified: 2026-08-23T17:06:27.662Z
---

When a problem or bug is found (in code, in a pipeline, in content), research on the web for the best/correct way to solve it before applying a fix, then execute the fix — don't just apply the first patch that comes to mind.

**Why:** User said this explicitly during the Mindset Mechanics project (2026-08-23) after a round of QA failures on generated video (character consistency issues) that required real investigation (comparing against published reference frames, reading VideoExpress feature docs) rather than a quick guess-and-patch. Reactive fixes without research had already failed twice on this project.

**How to apply:** Before proposing or executing a fix for any nontrivial problem, do a quick web/doc check for best practices or the tool's documented recommended approach, then act. Applies across projects, not just Mindset Mechanics. Doesn't require asking permission to search — just do the research as part of solving the problem, then execute.
