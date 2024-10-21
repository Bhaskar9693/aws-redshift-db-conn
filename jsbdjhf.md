# Migration Processes in Wizard

This document outlines the various types of migrations involved in the Wizard platform, detailing the processes for each type of change.

## Types of Migration

1. **Postgres Changes**
2. **Global/Local Filter Addition/Removal**
3. **Pinboard Level Change**
4. **New Pinboard Creation**
5. **Data Model Change**

---

## Detailed Migration Processes

### 1. Postgres Changes

#### Existing Report
- **Process:** Update existing reports (e.g., banners, KBQs, Additional Resources) in Postgres as per planned dates.
- **Time Required:** Approximately 0.5 to 3 hours, depending on the number of links that need updating.

#### New Banner
- **Process:** 
  - Update `report.csv` to include new banner details.
  - Insert these details into the registries table in Postgres.
  - Add verbiage as per requirements and verify against Jira.
- **Time Required:** 2 to 5 hours, depending on the number of banners.

#### New KBQ Report
- **Process:**
  - Update `report.csv` and insert new report details into the registries table.
  - Collaborate with the backend team to update `vw_WhizDynamicURLsPincards` view.
  - Verify the functionality of KBQ URLs.
- **Time Required:** 4 to 6 hours, depending on the number of KBQs added.

---

### 2. Filter/Pinboard/Pincard Change (Addition/Removal/Update)

#### Board Name Change
- **Process:** Use admin credentials to update board names directly in all environments.
- **Time Required:** Approximately 0.5 hours.

#### Filter/Pincard Change
- **Process:**
  - Migrations are performed on Thursdays per the respective story schedules.
  - Validate cascading between Prod board and Dev mockup board.
  - Export the Dev mockup board, update the JSON name to match the Prod main board, and import it into Prod.
  - Repeat for QA and Dev environments.
  - After migration, validate cascading and check functionality of added/removed/updated filters.
  - Compare QA and Prod boards for meaningful data consistency.
  
---

### 3. Pinboard Level Change

- **Process:** Similar to the filter/pincard change process:
  - Validate cascading before migrating.
  - Export, update JSON, and import the Dev mockup board into Prod.
  - Repeat for QA and Dev.
  - Post-migration, validate cascading and compare QA and Prod for data integrity.

---

### 4. New Pinboard Creation

- **Process:**
  - Migrations are performed on Wednesdays.
  - Export the Dev board, update the JSON name as required, and import into Prod.
  - Repeat for the QA environment.
  - After migration, validate cascading and ensure data integrity between QA and Prod boards.

---

### 5. Data Model Changes

- **Process:**
  - Data model changes are pushed to Bitbucket on Tuesdays for Prod and Thursdays for QA.
  - Data refresh activity occurs on Wednesdays for Prod, where changes are validated post-refresh.
  - Follow the standard migration process outlined above.

---

### Summary

This document summarizes the migration processes for the Wizard platform, ensuring a structured and consistent approach to managing changes across environments. Each migration type has specific procedures and timelines to ensure data integrity and system functionality.
