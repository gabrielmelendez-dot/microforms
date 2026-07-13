## Primary concepts

- **Layered decomposition** -- Split the repository into canonical capture, validation, harvesting, and knowledge-promotion layers so each component has one responsibility. (p. 2)
- **Hierarchical organization** -- Assign stable semantic responsibilities to top-level directories so the repository remains navigable and predictable. (p. 42)
- **Plain-text control plane** -- Use Markdown and YAML as the inspectable canonical record while confining binary material to evidence or artifact boundaries. (p. 25)

## Secondary concepts

- **Provenance modeling** -- Connect tasks, evidence, artifacts, actors, and promoted knowledge so every reusable conclusion traces to its production activity. (not in PDF; source: [W3C PROV-DM](https://www.w3.org/TR/prov-dm/))
- **Structural validation** -- Validate microform metadata against a declared schema before harvesting or promoting knowledge. (not in PDF; source: [JSON Schema Draft 2020-12 Validation](https://json-schema.org/draft/2020-12/json-schema-validation))
- **Globally unique identity** -- Assign UUIDv7 identifiers so concurrent writers can create time-ordered units without coordinating a shared sequence. (not in PDF; source: [RFC 9562](https://www.rfc-editor.org/rfc/rfc9562.html))
- **Append-only correction** -- Preserve validated history and represent material corrections through successor microforms and `supersedes` relationships. (not in PDF; general engineering practice)

## Tertiary concepts

- **Dot-directory convention** -- Keep repository-scoped Codex integration under `.agents/` so machine guidance does not dominate normal directory listings. (p. 22)
- **Generated views** -- Treat `catalog/` as disposable output that can be rebuilt from canonical microforms rather than as a competing source of truth. (not in PDF; general engineering practice)
- **Restricted-source boundary** -- Represent non-redistributable inputs with manifests, checksums, and local paths instead of committing them to a public repository. (not in PDF; general engineering practice)
