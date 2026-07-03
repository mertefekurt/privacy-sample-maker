# privacy-sample-maker

![privacy-sample-maker banner](assets/banner.svg)

`privacy-sample-maker` creates small synthetic CSV fixtures from a schema file. It is meant for docs, demos,
tests, and bug reports where you need realistic columns without copying customer data.

## Schema recipe

```csv
column,type,nullable,example
user_email,email,false,customer@example.com
signup_date,date,false,2026-01-31
plan,category,false,free|pro|enterprise
notes,text,true,
```

## Generate

```bash
privacy-sample-maker examples/schema.csv --rows 5 --seed 11
privacy-sample-maker examples/schema.csv --rows 5 --output sample.csv
```

## Supported types

`email`, `name`, `company`, `date`, `integer`, `category`, `uuid`, and `text`.

## Guardrail

Examples are treated as shape hints, not source values. For emails, names, companies, UUIDs, dates, and text,
the generator creates new deterministic values instead of echoing the example.

## Tests

The suite checks deterministic output, category handling, nullable fields, CSV rendering, no direct email copy,
and CLI help.

MIT.
