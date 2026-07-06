# Privacy Sample Maker

Generate realistic CSV fixtures from a schema without copying real customer data.

![Privacy Sample Maker cover](assets/readme-cover.svg)

## Schema in, sample rows out

```csv
column,type,nullable,example
user_email,email,false,customer@example.com
signup_date,date,false,2026-01-31
plan,category,false,free|pro|enterprise
notes,text,true,
```

```bash
git clone https://github.com/mertefekurt/privacy-sample-maker.git
cd privacy-sample-maker
python -m pip install -e ".[dev]"
privacy-sample-maker examples/schema.csv --rows 5 --seed 11
```

## Supported column types

`email`, `name`, `company`, `date`, `integer`, `category`, `uuid`, and `text`.

Examples are shape hints, not source values. The generator creates deterministic synthetic values instead of echoing sensitive examples back into the output.
