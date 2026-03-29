# Chapter 6: Integrations and Ecosystem

## Comprehensive Summary

Chapter 6 covers how to connect n8n with popular external platforms, focusing on authentication methods and practical integration patterns. The goal is to make all your tools "talk to each other" seamlessly.

### Popular Integrations Overview (6.1)

| App Family | Typical Use Cases | n8n Nodes | Auth Method |
|---|---|---|---|
| Google Workspace | Form data -> Sheets -> Email summary; auto-backup Drive files | Google Sheets, Gmail, Drive, Calendar | OAuth 2.0 |
| Social Media | Schedule posts, cross-post, scrape analytics | Twitter (X), LinkedIn, Facebook/Instagram Graph | OAuth 2.0 (+ long-lived tokens) |
| Productivity | Instant task creation, Slack notifications | Slack, Notion, Trello, Jira | OAuth 2.0 / API key |
| Comms and SMS | Send alerts, two-factor codes | Twilio, Send Email | API key, SMTP creds |

### Authentication Methods (6.2)

**OAuth 2.0 (The Digital Valet Key)**
- n8n never sees your password; you grant specific, limited permissions (e.g., "only read spreadsheets")
- Used by Google, LinkedIn, Twitter
- Access can be revoked instantly
- Modern and secure approach

**API Keys (The Master Key)**
- A single secret string that bypasses login
- Simpler but grants broader access
- Used by services like Twilio
- Requires careful management; n8n encrypts all stored keys

### Google Workspace Integration (6.3)
- Requires one-time OAuth Client ID setup
- **Google Sheets:** Append, update, read rows (lightweight database)
- **Gmail:** Send templated messages, monitor threads
- **Google Drive:** Upload reports, move files, share links
- **Google Calendar:** Auto-create events, fetch today's meetings

### Social Media Integration (6.4)
- **Content Adaptation:** One idea automatically adapted for LinkedIn (professional), Twitter (concise), Instagram (visual)
- **24/7 Monitoring:** Continuous brand mention and competitor update tracking with instant team alerts
- Requires developer portal access (Twitter app, Meta Business App) to obtain API credentials

### Project: Social Media Content Pipeline (6.5)

A workflow that takes a post idea from a Google Sheet and publishes across Twitter, LinkedIn, and Instagram simultaneously:

1. **Setup:** Credentials ready + Google Sheet with columns: Post, Image Link, Status
2. **Start Engine:** Manual Trigger (testing) or Schedule Trigger (e.g., weekday 9 AM)
3. **Find Next Idea:** Google Sheets "Get Rows" filtered to rows where Status is empty
4. **Label Maker:** Set Node assigns clean labels (caption, image_url)
5. **Parallel Post:** Three social media nodes connected simultaneously (Twitter, LinkedIn, Instagram Graph)
6. **Stop Repeat:** Final Google Sheets node updates Status to "Posted" for the processed row

## Key n8n Workflow Concepts

- OAuth 2.0 grants limited, revocable permissions without exposing passwords
- API keys provide direct access but require careful security management
- All credentials are encrypted in n8n's Credentials Manager
- Google integration requires one-time OAuth Client ID configuration
- Social media nodes require developer portal registration for API credentials
- Parallel node connections enable simultaneous cross-platform publishing
- Status tracking in Google Sheets prevents duplicate posting

## Practical Takeaways for Scientists

- **Google Sheets as lightweight database:** Scientists can use Sheets as the data backbone for automated workflows -- log experiment results, track sample processing status, or maintain publication lists
- **Automated data backup:** Set up workflows to auto-backup important Drive files or sync data across cloud storage platforms
- **Conference and publication alerts:** Use Gmail triggers to monitor for emails containing keywords like "accepted" or "review" and auto-create calendar events or Slack notifications
- **Research dissemination:** The Social Media Content Pipeline pattern can be adapted for sharing new publications, conference talks, or research highlights across academic social media (Twitter/X, LinkedIn, ResearchGate)
- **OAuth 2.0 is worth learning:** Many scientific data APIs (Google Earth Engine, institutional repositories) use OAuth; understanding it in n8n transfers to other contexts
- **Calendar automation:** Auto-create lab meeting events, equipment booking reminders, or deadline tracking from structured data sources

## Notable References

- Google Developer Console for OAuth setup
- Twitter Developer Portal
- Meta Business App (Facebook/Instagram)
- n8n Credentials Manager for secure key storage
