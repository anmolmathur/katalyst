# Phase 2 — Honest Assessment of the Platform Idea

_1 Sep 2026. Anmol's proposal: Supabase + Netlify application, analytics and client dashboards
on subdomains of katalystrm.com, AlikhiN connected to it, Nikhila taught to build features._

**Short version:** the direction is right and the commercial upside is real. The sequencing
worries me, one risk needs handling before anything goes near a subdomain, and the scope should
be about a third of what's described.

---

## Where I agree, without reservation

**Her data is relational and Sheets are the wrong shape for it.** This isn't a stylistic
preference. The audit made it concrete: 30 clients, ~730 contacts, six regional tabs, six
blogger tabs, coverage rows, publications, tiers, MAV rates — and sixteen of thirty brands
clustering under three restaurateurs. A contact belongs to a publication; a publication has a
tier and a rate; coverage links a client to a publication on a date; a client belongs to a
group. That is a schema begging to be written down, and every one of those relationships is
currently maintained by hand across tabs that can't reference each other.

The queries she cannot ask today are the valuable ones. *Which Tier 1 contacts have we not
placed anything with in six months? Which journalists cover more than one of our clients? What
did the Dugar group get this quarter versus last?* No amount of prompt engineering over
spreadsheets answers those reliably.

**Client-facing dashboards are the genuine commercial idea here.** Most agencies email a PDF
once a month. A live coverage portal at a client's own subdomain — updated continuously,
showing placements as they land — is a differentiator she could charge for, and it plays
directly to a positioning built on "reputation isn't managed, it's authored." That's the part
of this proposal I'd push *hardest* on, once the foundations are safe.

**And Supabase connects cleanly to Claude.** A Postgres she owns, queryable through an MCP
connector, is a far better substrate for AlikhiN than parsing spreadsheets. The integration
story is clean.

---

## Where I'd push back

### The tracker isn't empty because Sheets are bad

Twenty-four of thirty client tabs hold zero rows. The audit points at an unfired prerequisite —
thirty Google Alerts that were probably never created — plus search queries that collide on
generic brand names. **Migrating an empty pipeline into Postgres produces an empty Postgres.**

Storage is not the bottleneck. Ingestion is. If we build the platform first, the most likely
outcome is a beautiful, well-normalised, empty database, and a conversation in November about
why the dashboards show nothing.

### A custom application is the opposite of self-sustaining

Two turns ago we set the goal: her Claude account should sustain her own future requests after
you step back. A plugin serves that — files she can edit, versioned, that degrade gracefully.

An application does not. Schema migrations, auth, RLS policies, dependency updates, Supabase
deprecations, and the day something breaks at 9pm before a client review. She cannot maintain
any of that, and realistically neither can you at sustained volume — you have a CTO job, Bombay
Gothic, and this is a favour to a friend. **Every hour of app maintenance is an hour that
doesn't exist.**

That's not an argument against building it. It's an argument for building the smallest thing
that survives neglect.

### Her team writes in Sheets, and that's a feature

Pooja, Sazia and Disha add contacts to a spreadsheet. It's the one part of this system with
genuine multi-person adoption. Replace it with a database and you either lose their
contributions or you owe them a CRUD interface — forms, validation, permissions — which is a
much larger application than a dashboard, and the part most likely to go unfinished.

### The risk I'd insist on handling

**Her media list contains journalists' personal mobile numbers and home addresses.** I read one
in the sheet: a full residential address in Andheri West, alongside a mobile number, for a
named Condé Nast editor. Roughly 730 contacts, ~63% with emails, many with phones.

Putting that behind a public subdomain — or behind a Supabase project with a permissive row
level security policy, which is the single most common Supabase mistake — means a leak exposes
working journalists' home addresses. For a *reputation management* agency, that is not a bug,
it's an extinction-level story, and it would end relationships she has spent fifteen years
building.

So: **the media list never goes on a public subdomain, in any form.** Contact data stays
internal, behind authentication, with RLS written deliberately and tested. Client-facing pages
show coverage and analytics only — never the contact database. This is worth being rigid about.

### Free tiers won't carry a client-facing product

Supabase's free plan pauses a project after **one week of inactivity** and caps you at two
active projects. A client opening their dashboard on a quiet week gets nothing. The moment this
faces clients, it's Supabase Pro at $25/month — which is entirely affordable and worth it, but
it should be a decision, not a surprise.

---

## What I'd actually recommend

### Phase 2a — Postgres as a mirror, not a replacement

Sheets stay the system of record. A scheduled sync reads them into Supabase. Dashboards and
analytics read from Postgres. AlikhiN queries Postgres instead of parsing spreadsheets.

The team's workflow doesn't change. Nothing breaks if the app dies — the business carries on in
Sheets exactly as today. And you get the queries that are impossible now, immediately.

This is maybe a fifth of the work of the full idea and delivers most of the analytical value.

### Phase 2b — flip the media list to system-of-record

Only once 2a has proven itself, and only for the media list, where relational structure wins
most and a verification workflow (150 contacts marked Verify, with dates and history) is worth
real money to her. That needs a proper editing interface for the team, so treat it as its own
project with its own decision to start.

### Phase 2c — client portals

Last, and the commercial payoff. Per-client authenticated pages, coverage and analytics only,
no contact data, on subdomains. This is the thing worth charging for.

### The sequencing gift

**Phase 1 writes the schema for you.** Building the coverage tracker skill forces you to define
exactly what a coverage row is. Building the report builder defines what a monthly rollup needs.
Building per-client projects defines the client/group model. Do Phase 1 properly and the data
model falls out of it as a by-product, already validated against real use.

Design the schema first and you're guessing at what the work needs. That's the strongest
argument for finishing Phase 1 first, and it isn't a delay — it's the cheapest way to get the
design right.

---

## On teaching her to build features

Worth separating two things.

**Realistic and valuable:** teaching her to build Artifacts with Claude. She already started —
the IHCL dashboard — and asked exactly the right follow-up: "so we can build an actionable
one?" That is her building features, at a level she can genuinely sustain, with no deployment
and nothing to maintain. Every internal dashboard in Phase 2a could be an Artifact reading from
Postgres. I'd lean into this hard.

**Aspirational:** teaching her to ship features to a production application used by clients.
That's a real skill with a long runway, and framing it as achievable soon sets her up to feel
like she failed at something that was never a fair ask. If she wants it, it's a year-long
thread, not a Phase 2 deliverable.

The honest version: **she becomes the person who designs and specifies, and Claude becomes the
person who builds.** That matches how she already works — she wrote fifteen skills without
knowing what an agent was — and it scales far better than making her a part-time developer.

---

## Two things to resolve before any of this

**The two-master-lists question.** If the team is editing one sheet while automation reads
another, a sync will faithfully replicate the wrong data forever.

**The 31% marked Verify.** Migrating dirty data into a database makes the dirt permanent and
harder to fix — spreadsheets are genuinely easier to bulk-clean than a normalised schema with
foreign keys. Clean first, migrate second.

---

## Stack, if we proceed

Supabase for Postgres, auth, RLS and storage. Netlify for the front end and subdomains via
CNAME, which also consolidates the katalystrm.com and AlikhiN hosting we already planned to
tidy. Supabase's MCP connector wires Claude and AlikhiN to the data. Budget roughly $25/month
once anything faces a client, and treat the free tier as development-only given the one-week
pause.

All of that is sound. My only real argument is with the order.
