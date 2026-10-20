# Zalando RESTful API Guidelines — Summary

A condensed, scan-friendly digest of the [Zalando RESTful API and Event Guidelines](https://opensource.zalando.com/restful-api-guidelines/). Each section links back to the original for the full rule text and examples.

> Source: <https://opensource.zalando.com/restful-api-guidelines/>
> Rule numbers in parentheses (e.g. `#100`) match Zalando's rule anchors — append them to the source URL for the canonical wording.

---

## TL;DR — the ten rules that hurt most if you skip them

- **API-first**: design and review the OpenAPI spec *before* writing code (#100).
- **OpenAPI 3.x**, single self-contained YAML, published in the API repo (#101, #192).
- **URLs** are lowercase **kebab-case**, **noun-based**, **plural** collections; actions go in HTTP methods, not paths (#129, #134, #141).
- **JSON**: `snake_case` property names, plural arrays, standard field names (`id`, `xyz_id`, `etag`) (#118, #120, #174).
- **Errors**: RFC 7807 `application/problem+json` for every non-2xx response (#176).
- **Status codes**: use the official IANA set; stick to the common ones (200/201/204/400/401/403/404/409/500) unless there's a real reason (#150, #243).
- **Versioning**: SemVer in the spec's `info.version`; MAJOR bump only for breaking changes (#116).
- **Compatibility**: **don't break clients** — extend, don't mutate; be conservative in what you send, tolerant in what you accept (#106, #107, #108, #109).
- **Pagination**: always paginate collections; prefer **cursor-based** over offset (#159, #160).
- **Security**: every endpoint behind Bearer/OAuth2 with a scope named `<app-id>.<resource>.<access-mode>` (#104, #105, #225).

---

## 1. Introduction

Zalando's guidelines exist so their (hundreds of) microservices expose consistent, durable APIs. The rule keywords follow **RFC 2119** — `MUST` / `SHOULD` / `MAY` — so you can grep for the hard requirements.

Read more: <https://opensource.zalando.com/restful-api-guidelines/#introduction>

## 2. Principles

- **REST-based APIs with JSON payloads** are the default.
- **API as a product** — optimise for developer experience and long-term consistency, not for the internal team's convenience.
- **API First** — the API contract is a first-class deliverable, defined and reviewed before implementation.

Read more: <https://opensource.zalando.com/restful-api-guidelines/#api-design-principles>

## 3. Basic Terminology

- **API specification** is written in **OpenAPI 3.x** (OAS).
- The spec is normative; the deployed service may lag or diverge — the spec is what clients contract against.
- Distinguish **API** (contract) from **implementation** (running service).

Read more: <https://opensource.zalando.com/restful-api-guidelines/#basic-terminology>

## 4. General Guidelines

- **MUST follow API First** (#100) — design → peer-review → implement.
- **MUST provide OpenAPI specification** (#101) as a single self-contained YAML.
- **SHOULD provide API user manual** (#102) with scope, examples, edge cases.
- **MUST write in US English** (#103).
- **MUST only use durable remote refs** (#234) — no links to mutable sources.

Read more: <https://opensource.zalando.com/restful-api-guidelines/#general-guidelines>

## 5. REST Basics — Meta Information

- **MUST include meta info** in the spec (#218): title, version, description, contact, `x-api-id`, `x-audience`.
- **MUST use SemVer** for `info.version` (#116): MAJOR = breaking, MINOR = additive, PATCH = fix.
- **MUST provide immutable API ID** (#215) in URN-like form, matching `^[a-z0-9][a-z0-9-:.]{6,62}[a-z0-9]$`.
- **MUST declare `x-audience`** (#219): `component-internal`, `business-unit-internal`, `company-internal`, `external-partner`, or `external-public`.
- **MUST apply functional naming** (#223) for hostnames and event names, scaled to the audience.

Read more: <https://opensource.zalando.com/restful-api-guidelines/#meta-information>

## 6. REST Basics — Security

- **MUST secure endpoints** (#104) with Bearer/OAuth2.
- **MUST define and assign permissions (scopes)** (#105); use the `uid` pseudo-scope for user-only access.
- **MUST follow scope naming** `<application-id>.<resource-name>.<access-mode>` — e.g. `order-management.sales-order.read` (#225).

Read more: <https://opensource.zalando.com/restful-api-guidelines/#security>

## 7. REST Basics — Data Formats

- **MUST use standard formats** (#238) — ISO/IETF for dates, times, numbers, binary.
- **MUST specify number/integer format** (#171): `int32`, `int64`, `bigint`, `float`, `double`, `decimal`.
- **MUST use RFC 3339 date-time** with uppercase `T` and `Z` (#169).
- **MUST use ISO codes** (#170): `ISO 3166-1 alpha-2` (country), `ISO 639-1` (language), `ISO 4217` (currency).
- **SHOULD only use UUIDs when necessary** (#144) — server-generated IDs are often better for low-volume master data.

Read more: <https://opensource.zalando.com/restful-api-guidelines/#data-formats>

## 8. REST Basics — URLs

- **MUST pluralise resource names** (#134); use cardinality constraints for singletons.
- **MUST use kebab-case for path segments** (#129), matching `^[a-z][a-z\-0-9]*$`.
- **MUST keep URLs verb-free** (#141) — actions belong in HTTP methods.
- **MUST think in resources, not actions** (#138).
- **MUST use snake_case for query parameters** (#130) — same convention as JSON properties.

Read more: <https://opensource.zalando.com/restful-api-guidelines/#urls>

## 9. REST Basics — JSON Payload

- **MUST use JSON** (#167), RFC 7159 / RFC 7493.
- **MUST always return JSON objects as top-level data structures** (#110) — never a bare array at the root, even for collections. Wrap in `{ "items": [...] }` so the shape stays extensible (e.g. adding `next`/`prev` later is non-breaking).
- **MUST use snake_case property names** (#118), matching `^[a-z_][a-z_0-9]*$`.
- **SHOULD pluralise array names** (#120).
- **MUST use common field names** (#174): `id`, `<entity>_id`, `etag`, `created`, `modified`.
- **MUST use common money object** (#173): `{ amount: decimal, currency: ISO-4217 }`.

Read more: <https://opensource.zalando.com/restful-api-guidelines/#json-guidelines>

## 10. REST Basics — HTTP Requests

- **MUST use HTTP methods correctly** (#148) — GET/POST/PUT/PATCH/DELETE per REST semantics.
- **SHOULD design POST/PATCH to be idempotent** (#229) for safe retries (idempotency keys).
- **MUST define collection format** for header/query params (#154).
- **SHOULD design simple query languages via parameters** (#236); avoid ad-hoc DSLs.
- **MUST document implicit response filtering** (#226) — e.g. auth-based row filtering.
- **MUST NOT use GET with a body for queries** — bodies on GET requests are stripped by many proxies/CDNs and have undefined semantics. Use one of:
  - **Query parameters** for simple key/value filters (#236) — `GET /orders?status=shipped&customer_id=123`
  - **`POST /resource/searches`** for complex queries with nested filters or boolean logic (#237) — accepts a JSON body, returns the same paged envelope as a collection GET. Using a noun sub-resource (`/searches`) keeps URLs verb-free (#141).
  - **`QUERY` method** (RFC 9110, emerging) — semantically safe + idempotent GET with a body; not yet widely supported, prefer `POST /searches` for now.

Read more: <https://opensource.zalando.com/restful-api-guidelines/#http-requests>

## 11. REST Basics — HTTP Status Codes

- **MUST use official IANA status codes** (#243).
- **MUST specify all success and error responses** in OpenAPI (#151).
- **SHOULD only use common codes** (#150) — 200/201/202/204, 301/303/304, 400/401/403/404/405/409/410/412/415/423/429, 500/501/503.
- **MUST use 207 Multi-Status** for batch/compound operations (#152).
- **MUST support `application/problem+json`** per RFC 7807 for errors (#176).

Read more: <https://opensource.zalando.com/restful-api-guidelines/#http-status-codes-and-errors>

## 12. REST Basics — HTTP Headers

- **MUST use `Content-*` headers correctly** (#178).
- **SHOULD use Hyphenated-Pascal-Case for HTTP headers** (#132) — e.g. `X-Flow-Id`.
- **SHOULD prefer `Location` over `Content-Location`** (#180).
- **MUST propagate proprietary headers** (#184) end-to-end through the call chain.
- **MUST support `X-Flow-ID`** (#233) for distributed tracing / log correlation.

Read more: <https://opensource.zalando.com/restful-api-guidelines/#headers>

## 13. REST Design — Hypermedia

- **MUST target REST maturity level 2** (#162) — resources + HTTP verbs + status codes.
- **MAY use level 3 (HATEOAS)** (#163) — but not required.
- **MUST use common hypertext controls** (#164) when embedding links.
- **SHOULD use simple hypertext controls** for pagination and self-refs (#165).
- **MUST use full absolute URI** for resource identifiers in links (#217).

Read more: <https://opensource.zalando.com/restful-api-guidelines/#hypermedia>

## 14. REST Design — Performance

- **SHOULD reduce bandwidth and improve responsiveness** (#155) — pick the smallest useful representation.
- **SHOULD support gzip compression** (#156).
- **SHOULD support partial responses via field filtering** (#157) — `?fields=…`.
- **SHOULD allow embedding sub-resources** (#158) — `?embed=…`.
- **MUST document cacheability** for `GET`, `HEAD`, and `POST` (#227), including `Cache-Control`, `Vary`, `ETag`.

Read more: <https://opensource.zalando.com/restful-api-guidelines/#performance>

## 15. REST Design — Pagination

- **MUST support pagination** for any collection that can grow (#159).
- **SHOULD prefer cursor-based pagination**; avoid offset for large data sets (#160).
- **SHOULD use a standard page response object** (#248) with `items` + `next`/`prev` cursors.
- **SHOULD use pagination links** (#161) — HATEOAS-style `next`/`prev` URLs.
- **SHOULD avoid returning a total count** for large sets (#254) — it's expensive.

Read more: <https://opensource.zalando.com/restful-api-guidelines/#pagination>

## 16. REST Design — Compatibility

- **MUST NOT break backward compatibility** (#106).
- **SHOULD prefer compatible extensions** (#107) — add optional fields rather than change existing ones.
- **SHOULD design APIs conservatively** (#109) — small, well-defined interfaces evolve better.
- **MUST prepare clients to accept compatible extensions** (#108) — unknown fields must be ignored.
- **MUST treat the OpenAPI spec as open for extension by default** (#111).

Read more: <https://opensource.zalando.com/restful-api-guidelines/#compatibility>

## 17. REST Design — Deprecation

- **MUST reflect deprecation in the spec** (#187).
- **MUST obtain client approval before shut-down** (#185); **MUST collect external-partner consent on the sunset date** (#186).
- **MUST monitor usage of deprecated APIs** scheduled for sunset (#188).
- **SHOULD add `Deprecation` and `Sunset` headers** to responses (#189) and monitor them client-side (#190).
- **MUST NOT start using a deprecated API** (#191).

Read more: <https://opensource.zalando.com/restful-api-guidelines/#deprecation>

## 18. REST Operation

- **MUST publish the OpenAPI spec** for any deployed API (#192) — typically to an internal API registry.
- **SHOULD monitor API usage** (#193) so deprecation and capacity decisions are data-driven.

Read more: <https://opensource.zalando.com/restful-api-guidelines/#api-operation>

## 19. EVENT Basics — Event Types

- Events are part of the **service interface** — hold them to the same standard as REST endpoints.
- **MUST define events compliant with the API guidelines** (#208) and **treat events as part of the service interface** (#194).
- **MUST specify and register events as event types** (#197) and **make the schema available for review** (#195).
- **MUST follow the event type naming convention** (#213) and **indicate ownership** (#207).
- **MUST version event schemas with SemVer** (#246); **SHOULD avoid `additionalProperties`** (#210).

Read more: <https://opensource.zalando.com/restful-api-guidelines/#events>

## 20. EVENT Basics — Event Categories

- **MUST conform to a category** (#198): general event, data change event, etc.
- **MUST provide mandatory event metadata** (#247) and **unique event IDs** (#211).
- **MUST use general events for business process steps** (#201); **MUST use data change events for mutations** (#202).
- **MUST provide explicit ordering** for data change events (#242); **SHOULD** do the same for general events (#203).
- **SHOULD use hash partition strategy** for data change events (#204) to keep per-entity order intact.

Read more: <https://opensource.zalando.com/restful-api-guidelines/#event-categories>

## 21. EVENT Design

- **MUST be robust against duplicates** when consuming (#214) — assume at-least-once delivery.
- **MUST define events around useful business resources** (#199), not internal implementation details.
- **MUST maintain backward compatibility** for events (#209) — same rules as REST.
- **SHOULD avoid sensitive data in events** (#200).
- **SHOULD design consumers for idempotent, out-of-order processing** (#212).
- **SHOULD align data change events with the API's resource shape** (#205).

Read more: <https://opensource.zalando.com/restful-api-guidelines/#events-design>

## 22. Appendix A — References

Pointers to the RFCs, ISO standards, and OpenAPI spec that the rules build on (RFC 2119, 3339, 7159, 7231, 7807, ISO 4217, etc.).

Read more: <https://opensource.zalando.com/restful-api-guidelines/#appendix-references>

## 23. Appendix B — Tooling

- API-first workflow tooling (OpenAPI editors, linters, mock servers).
- Support libraries that enforce the guidelines at build time — e.g. **[Zally](https://github.com/zalando/zally)**, Zalando's OpenAPI linter.

Read more: <https://opensource.zalando.com/restful-api-guidelines/#appendix-tooling>

## 24. Appendix C — Best Practices

Worked patterns for the trickier design areas:

- Cursor-based pagination.
- Optimistic locking with `ETag` / `If-Match`.
- Handling compatible API extensions in clients and servers.
- Modelling time intervals.

Read more: <https://opensource.zalando.com/restful-api-guidelines/#appendix-best-practices>

## 25. Appendix D — Changelog

Chronological log of rule additions, promotions (SHOULD → MUST), and clarifications. Worth skimming when a lint rule changes in **Zally** or when your team last audited the spec more than ~6 months ago.

Read more: <https://opensource.zalando.com/restful-api-guidelines/#appendix-changelog>

---

## Quick links

- Full guidelines: <https://opensource.zalando.com/restful-api-guidelines/>
- Zally linter: <https://github.com/zalando/zally>
- OpenAPI Specification: <https://spec.openapis.org/oas/latest.html>
- RFC 7807 Problem Details: <https://datatracker.ietf.org/doc/html/rfc7807>
- RFC 3339 Date/Time: <https://datatracker.ietf.org/doc/html/rfc3339>
