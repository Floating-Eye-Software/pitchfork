────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

• Here’s the clean split I’d make from the last two turns in the chat.

  The key point is in [/home/mlehotay/projects/pitchfork/_work/pitchfork-expansion-chat.md:359] through [/home/mlehotay/
  projects/pitchfork/_work/pitchfork-expansion-chat.md:648]: the work is now three separate artifacts, not one blob.

  What to do now

  - Write the architecture docs first.
  - Preserve the RPG lore in its own home.
  - Keep the RPG client/spec work as a separate mechanics/spec track.

  1) Create these docs now

  - [/home/mlehotay/projects/pitchfork/docs/pitchfork-symbolic-frequencies.md]
  - [/home/mlehotay/projects/pitchfork/docs/pitchfork-symbolic-crafting.md]
  - [/home/mlehotay/projects/pitchfork/docs/pancakes-place-model.md]
  - [/home/mlehotay/projects/pitchfork/docs/pancakes-reference-services.md]
  - [/home/mlehotay/projects/pitchfork/docs/pancakes-node-capabilities.md]
  - [/home/mlehotay/projects/pitchfork/docs/rpg/README.md]
  - [/home/mlehotay/projects/pitchfork/docs/rpg/story.md]
  - [/home/mlehotay/projects/pitchfork/docs/rpg/world.md]
  - [/home/mlehotay/projects/pitchfork/docs/rpg/academy.md]
  - [/home/mlehotay/projects/pitchfork/docs/rpg/mentors.md]
  - [/home/mlehotay/projects/pitchfork/docs/rpg/magic.md]
  - [/home/mlehotay/projects/pitchfork/docs/rpg/chapters/01-colored-tokens.md] through 08-restoring-balance.md

  2) Create plans for the rest

  - Use the existing RPG client migration plan [/home/mlehotay/projects/pitchfork/_work/plans/0002-pitchfork-rpg-client-
    spec-update.md] for mechanics/spec updates only.

  - Create a new plan for symbolic architecture foundations covering:
      - pitchfork-symbolic-frequencies.md
      - pitchfork-symbolic-crafting.md
      - pancakes-place-model.md
      - pancakes-reference-services.md
      - pancakes-node-capabilities.md

  - Create a new plan for RPG lore preservation covering:
      - the docs/rpg/ directory
      - preserving Blanken, token/value separation, contracts, smart-contract metaphor, and restoring balance

  - Optionally create a smaller follow-on plan for application docs:
      - pitchfork-frequencies.md
      - pitchfork_economics.md
      - pitchfork_rpg_client.md
      - pitchfork_client_api_spec.md
      - pancakes_node_infrastructure.md
      - pancakes_client_node_architecture.md
      - pancakes_service_exchange.md
      - pancakes-goods-and-services-model.md
      - pancakes-open-gis.md
      - pancakes-open-barcodes.md
      - lone-honk-observation.md
      - lone-honk-ecology.md

  3) Add context copypastas

  - Keep the three existing ones:
      - Symbolic Frequencies
      - Place Model
      - Capability Model

  - Add a fourth copypasta for RPG lore preservation, since the chat makes that a separate workstream:
      - “Preserve the lore sequence: colored token -> Blanken -> gray token + released value -> contracts -> commodities
        -> Ether -> smart contracts -> restored balance.”

      - Include the rule that the lore is preserved, not rewritten, and that the old blockchain ending should be
        modernized to community-governed civic infrastructure.

  4) Don’t merge these tracks

  - Don’t fold lore into the RPG client spec.
  - Don’t make the architecture depend on the lore.
  - Don’t treat docs/rpg/ as just another mechanics dump.

  If you want, I can next turn this into concrete _work/plans/*.md entries and a minimal todo breakdown.

─ Worked for 1m 13s ────────────────────────────────────────────────────────────────────────────────────────────────────
