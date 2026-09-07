# Web Traffic Analytics — Project Report

## Objective
Evaluate website user behavior and engagement using session, page-path, traffic-source and funnel analysis.

## Dataset
Synthetic Google Analytics-style data is included because no real GA export was provided.
- Sessions: 5,000
- Date range: 2026-01-01 to 2026-03-31
- Session dataset: `data/web_traffic_sessions.csv`
- Page-path dataset: `data/page_path_events.csv`

## KPI Summary
| KPI | Result |
|---|---:|
| Sessions | 5,000 |
| Bounce rate | 43.1% |
| Engagement rate | 56.9% |
| Avg pages/session | 2.75 |
| Avg session duration | 116.5 sec |
| Signup conversion | 7.3% |

## Traffic Source Analysis
| channel        |   sessions |   bounce_rate |   conversion |
|:---------------|-----------:|--------------:|-------------:|
| Organic Search |       1644 |         0.415 |        0.078 |
| Direct         |       1205 |         0.363 |        0.082 |
| Paid Search    |        768 |         0.516 |        0.062 |
| Social         |        588 |         0.578 |        0.049 |
| Referral       |        398 |         0.432 |        0.085 |
| Email          |        397 |         0.315 |        0.063 |

## Landing Page Analysis
| landing_page   |   sessions |   bounce_rate |   conversion |
|:---------------|-----------:|--------------:|-------------:|
| /products      |       1226 |         0.397 |        0.11  |
| /blog          |        916 |         0.495 |        0.012 |
| /              |        902 |         0.433 |        0.03  |
| /pricing       |        764 |         0.351 |        0.114 |
| /features      |        763 |         0.461 |        0.126 |
| /contact       |        429 |         0.473 |        0.019 |

## Funnel
- **Sessions:** 5,000 users
- **Product View:** 3,265 users — 34.7% drop-off
- **Pricing View:** 1,528 users — 53.2% drop-off
- **Signup Started:** 627 users — 59.0% drop-off
- **Signup Completed:** 364 users — 41.9% drop-off

### Largest drop-off
The largest relative drop-off is between **Pricing View → Signup Started**, at **59.0%**. This is the first area to investigate for UX/CRO improvements.

## Recommended Actions
1. Audit high-bounce, high-traffic landing pages.
2. Compare mobile versus desktop engagement and conversion.
3. Improve the highest-drop-off funnel step with clearer CTAs, reduced friction and stronger trust signals.
4. Shift acquisition focus toward channels with strong conversion quality, not just high volume.
5. Use page-path and session-recording tools to validate why users leave.
6. Repeat the analysis over time and after UX changes.

## Skills Demonstrated
Funnel analysis, session analysis, page-path analysis, traffic-source analysis, bounce-rate analysis, engagement metrics, visualization, drop-off identification and UX recommendations.
