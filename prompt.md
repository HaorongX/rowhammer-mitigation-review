You are assisting with a literature review on RowHammer mitigations.

In your responses, I need you to tag each source that describes a RowHammer mitigation according to the mitigation strategies used in that work. Make sure to use EVERY source.

Tagging Rules

Each source may receive multiple tags.

You may assign as many tags as necessary, as long as each tag is justified by the content of the source.

Only assign tags that accurately describe the mitigation approach used in the source.

If a source describes multiple mitigations in extensive details, then independently assign tags to each mitigation. If any mitigations in this work are apparently not the focus of the work, do not include it in your output.

Available Tags and Definitions

1. Long-term
Mitigations that aim to prevent RowHammer in DRAM manufactured in the future. It often involves changing the design and structure of DRAM or other hardware that cannot be easily added to existing hardware.

2. Short-term
Mitigations that aim to prevent RowHammer in existing DRAM devices, which can come into effect by firmware update etc. It must be possible to push the mitigations to terminal users as an update for a mitigation to be considered short-term.

3. Hardware-based
Mitigations implemented entirely in hardware (e.g., within DRAM chips, memory controllers, or other hardware logic).

4. Software-based
Mitigations implemented entirely in software (e.g., OS mechanisms, compilers, runtime systems).

5. Software–hardware co-designed
Mitigations that require cooperation between software and hardware components.

6. Isolation-Centric
Mitigations that prevent RowHammer attacks by isolating potential aggressor and victim rows across trust domains.
Example: placing guard rows between rows belonging to different domains.

Example system: ZebRAM, which inserts restricted-use guard rows between potential aggressor–victim pairs.

Note: Isolation-centric defenses typically do not prevent intra-domain disturbances (i.e., hammering within the same domain).

7. Frequency-Centric
Mitigations that prevent RowHammer by limiting the frequency of row activations (ACT commands).
These approaches ensure that the number of activations to any row within a refresh interval remains below the MAC (Minimum ACT Count required to induce a bit flip).
Example: BlockHammer, which rate-limits row activations using memory-controller counters.

8. Refresh-Centric
Mitigations that proactively refresh potential victim rows before bit flips occur.
These systems use hardware and/or software mechanisms to identify potential victim rows and refresh them before aggressor rows reach the MAC threshold.

Output Format

For each source:

Source: <paper title or citation>


- [Mitigation 1]
    - Tag 1
    - Tag 2
    - Tag 3
    - etc.
- - [Mitigation 2]
    - Tag 1
    - Tag 2
    - Tag 3
    - etc.
- ...

- Excluded: [List of mitigations not discussed because they are not the focus of the work]

Justification:
Brief explanation of why the source fits each assigned tag.