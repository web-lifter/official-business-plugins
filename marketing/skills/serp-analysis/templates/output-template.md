# SERP Analysis — "{{query}}"

**Region:** {{region}} | **Device:** {{device}} | **Date:** {{date_dd_mm_yyyy}}
**Personalisation:** Off | **API Source:** SerpAPI

---

## Query Metadata

| Field | Value |
|---|---|
| Query | `{{query}}` |
| Google locale | {{locale_code}} |
| Estimated monthly volume | {{volume}} |
| Keyword difficulty | {{difficulty}} |
| Total organic results (approx.) | {{organic_result_count}} |
| Paid ads present | {{ads_present}} ({{ads_count}} ads) |

---

## Dominant Search Intent

**Primary Intent:** {{primary_intent}}
**Sub-Intent:** {{sub_intent}}
**Intent Confidence:** {{intent_confidence}} — {{intent_rationale}}

{{#if mixed_intent}}
**Mixed Intent Signal:** {{mixed_intent_note}}
{{/if}}

---

## SERP Features Present

| Feature | Present | Content / Source | Position | Rankable? |
|---|---|---|---|---|
| AI Overview | {{ai_overview_present}} | {{ai_overview_source}} | {{ai_overview_position}} | {{ai_overview_rankable}} |
| Featured Snippet | {{fs_present}} | {{fs_source}} | {{fs_position}} | {{fs_rankable}} |
| People Also Ask | {{paa_present}} | {{paa_count}} questions | {{paa_position}} | {{paa_rankable}} |
| Local Pack | {{lp_present}} | {{lp_businesses}} | {{lp_position}} | {{lp_rankable}} |
| Video Pack | {{vp_present}} | {{vp_source}} | {{vp_position}} | {{vp_rankable}} |
| Image Pack | {{ip_present}} | — | {{ip_position}} | {{ip_rankable}} |
| Shopping | {{shop_present}} | — | {{shop_position}} | N/A (paid) |
| Knowledge Panel | {{kp_present}} | {{kp_entity}} | Right rail | {{kp_rankable}} |
| Top Stories | {{ts_present}} | {{ts_source}} | {{ts_position}} | {{ts_rankable}} |

### People Also Ask Questions
{{#if paa_present}}
1. {{paa_q_1}}
2. {{paa_q_2}}
3. {{paa_q_3}}
4. {{paa_q_4}}
{{/if}}

---

## Top 10 Organic Results

| # | Title | Domain | Format | Schema | Snippet |
|---|---|---|---|---|---|
| 1 | {{r1_title}} | {{r1_domain}} | {{r1_format}} | {{r1_schema}} | {{r1_snippet}} |
| 2 | {{r2_title}} | {{r2_domain}} | {{r2_format}} | {{r2_schema}} | {{r2_snippet}} |
| 3 | {{r3_title}} | {{r3_domain}} | {{r3_format}} | {{r3_schema}} | {{r3_snippet}} |
| 4 | {{r4_title}} | {{r4_domain}} | {{r4_format}} | {{r4_schema}} | {{r4_snippet}} |
| 5 | {{r5_title}} | {{r5_domain}} | {{r5_format}} | {{r5_schema}} | {{r5_snippet}} |
| 6 | {{r6_title}} | {{r6_domain}} | {{r6_format}} | {{r6_schema}} | {{r6_snippet}} |
| 7 | {{r7_title}} | {{r7_domain}} | {{r7_format}} | {{r7_schema}} | {{r7_snippet}} |
| 8 | {{r8_title}} | {{r8_domain}} | {{r8_format}} | {{r8_schema}} | {{r8_snippet}} |
| 9 | {{r9_title}} | {{r9_domain}} | {{r9_format}} | {{r9_schema}} | {{r9_snippet}} |
| 10 | {{r10_title}} | {{r10_domain}} | {{r10_format}} | {{r10_schema}} | {{r10_snippet}} |

### Content Format Mix

| Format | Count | % of Top 10 |
|---|---|---|
| {{format_1}} | {{format_1_count}} | {{format_1_pct}} |
| {{format_2}} | {{format_2_count}} | {{format_2_pct}} |

**Dominant format (top 3):** {{dominant_format}}

---

## SERP Volatility

**Rating:** {{volatility_rating}} ({{volatility_rationale}})

---

## Ranking Opportunity Assessment

**Competitive Difficulty:** {{difficulty_rating}} — {{difficulty_rationale}}

### Recommended Content Approach

| Element | Recommendation |
|---|---|
| Format | {{recommended_format}} |
| Target word count | {{recommended_word_count}} |
| Recommended H1 | `{{recommended_h1}}` |
| Recommended title tag | `{{recommended_title}}` |
| Target SERP features | {{target_serp_features}} |
| Schema to implement | {{recommended_schema}} |

### SERP Feature Opportunities

{{#if fs_opportunity}}
**Featured Snippet:** {{fs_opportunity_detail}}
{{/if}}

{{#if paa_opportunity}}
**PAA gaps** — these questions are not well-answered by current top results:
- {{paa_gap_1}}
- {{paa_gap_2}}
{{/if}}

{{#if ai_overview_opportunity}}
**AI Overview:** {{ai_overview_opportunity_detail}}
{{/if}}

---

## Related Searches

{{related_searches}}

---

## Strategic Recommendation

{{strategic_recommendation}}
