• Concrete work order, in the order I would execute it:

  1. Sync the planning surfaces first.

  - In /home/mlehotay/projects/pitchfork/_work/plans/plans.csv, add
    0005-rpg-lore-preservation so the new plan file is discoverable.
  - In /home/mlehotay/projects/pancakes/_work/plans/plans.csv, add
    0009-symbolic-architecture-foundations as ready and
    0010-application-documentation-migration as blocked on 0009 so the
    execution order is visible in the dashboard.

  2. Build the new foundation docs in pancakes next.

  Strategy:

  - Write the foundation docs in dependency order so each later document can
    reference earlier terminology instead of redefining it.
  - Start with /home/mlehotay/projects/pancakes/docs/pitchfork-symbolic-frequencies.md
    as the canonical vocabulary anchor.
  - Follow with /home/mlehotay/projects/pancakes/docs/pitchfork-symbolic-crafting.md
    so symbolic transformation has a stable basis.
  - Then write /home/mlehotay/projects/pancakes/docs/pancakes-place-model.md
    because place and stewardship shape how later reference and capability
    documents should interpret the world.
  - Next write /home/mlehotay/projects/pancakes/docs/pancakes-reference-services.md
    to separate public facts from private node state.
  - Finish the foundation with
    /home/mlehotay/projects/pancakes/docs/pancakes-node-capabilities.md as the
    extension mechanism built on top of the earlier primitives.
  - For each document, use the same internal structure: canonical definition,
    non-goals, examples, and a short "what later docs should reference"
    section.
  - After each document, do a cross-reference pass to remove any accidental
    redefinitions and push application-specific material into the later
    migration docs.

  3. Preserve the RPG lore in pitchfork as a separate track.

  - Build docs/rpg/README.md first.
  - Then docs/rpg/story.md, docs/rpg/world.md, docs/rpg/academy.md, docs/rpg/mentors.md, and docs/rpg/magic.md.
  - Then write the chapter sequence in order: 01-colored-tokens through 08-restoring-balance.

  4. Update Pitchfork’s application docs after the foundations exist.

  - docs/pitchfork-frequencies.md
  - docs/pitchfork_economics.md
  - docs/pitchfork_rpg_client.md
  - docs/pitchfork_client_api_spec.md

  5. Update Pancakes’ application docs after the foundation docs are stable.

  - /home/mlehotay/projects/pancakes/docs/pancakes_node_infrastructure.md
  - /home/mlehotay/projects/pancakes/docs/pancakes_client_node_architecture.md
  - /home/mlehotay/projects/pancakes/docs/pancakes_service_exchange.md
  - /home/mlehotay/projects/pancakes/docs/pancakes-goods-and-services-model.md
  - /home/mlehotay/projects/pancakes/docs/pancakes-open-gis.md
  - /home/mlehotay/projects/pancakes/docs/pancakes-open-barcodes.md

  6. Finish with Lone Honk.

  - /home/mlehotay/projects/pancakes/docs/lone-honk-observation.md
  - /home/mlehotay/projects/pancakes/docs/lone-honk-ecology.md

  Parallelism:

  - Steps 2 and 3 can run in parallel if you want to split the work by repo.
  - Steps 4, 5, and 6 should wait until the foundation docs are in place.
