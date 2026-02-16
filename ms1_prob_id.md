# Milestone 1 – Problem Identification

## 1. Unknown / Wrong / Inconsistent Data

While reviewing the dataset structure, we identified the following possible issues:

- Missing values in some columns (blank fields).
- Duplicate athlete entries appearing across multiple events.
- Inconsistent formatting between Paris dataset and original data files.
- Possible invalid numeric values in medal or edition fields.
- Inconsistent NOC codes or country names.

---

## 2. Handling Wrong / Unknown Data

We plan to handle incorrect or missing data as follows:

- Missing values will be left blank or replaced with "Unknown" where appropriate.
- Invalid numeric fields will be validated before processing.
- Duplicate athlete entries will be detected using `athlete_id` as a unique identifier.
- Inconsistent country/NOC codes will be standardized during cleaning.

---

## 3. Organization of Paris Data

The Paris dataset is expected to be organized by:

- edition
- edition_id
- NOC (country code)
- athlete records

To maintain consistency with the original dataset:

- Paris data will be normalized to match column structure.
- Key fields such as athlete_id and edition_id will be used for mapping.
- Output structure will strictly follow the required schema.

---

## 4. Detecting Duplicate Athlete Entries

Duplicate detection strategy:

- Use athlete_id as a primary key.
- Store processed athlete IDs in a set/dictionary.
- Skip duplicate records during processing.

---

## 5. How We Will Verify the Application

To verify correctness:

- Confirm that all 5 required output files are created.
- Check that medal tally header matches the exact required format.
- Confirm that the event results file includes the "age" column.
- Perform spot checks on sample records.
