# Sports data provenance and freshness

This guide defines how the NBC Soka project should communicate the origin and freshness of sports data.

## Source attribution
- Record the upstream provider or official competition source for each imported dataset.
- Preserve source identifiers and retrieval timestamps where practical.
- Do not present scraped or third-party content as official league data unless the source confirms it.
- Respect provider terms, robots policies, and applicable rate limits.

## Freshness
- Display the last successful update time for schedules, standings, and match results.
- Distinguish live data, recently synchronized data, and cached historical data.
- Do not label stale cached results as live.
- Define a reasonable refresh interval per data type and avoid unnecessary polling.

## Data quality
- Validate team and competition identifiers before joining datasets.
- Handle postponed, abandoned, rescheduled, and completed matches as distinct states.
- Preserve timezone context and display local kickoff times consistently.
- Detect duplicate events and conflicting scores before publication.

## Failure handling
When a source is unavailable, retain the last known good dataset with a visible stale indicator. Log the failed retrieval and retry with bounded backoff. Never fabricate scores, fixtures, or standings to fill missing data.

## Review
Record the source, retrieval time, validation outcome, and any manual correction. Require a second review for manual score or result corrections.
