# Chapter 8: Document and Task Management

## Comprehensive Summary

Chapter 8 covers two major automation domains: (1) document and file management, and (2) task and project management. The chapter demonstrates how AI can transform unstructured files and communications into organized, actionable systems.

### Document and File Automation (8.1)

**AI-Powered File Organization (Project: Mistral AI File Organizer)**
A workflow that automatically organizes files using AI intelligence:
1. **Local File Trigger:** Monitors a folder (e.g., Downloads) for new files
2. **Set Variables:** Stores the directory path for reuse
3. **Get Files and Folders:** Lists all files using `ls` command
4. **Convert to Array:** Transforms text output into structured file/folder lists
5. **If Has Target Files:** Checkpoint to verify files exist before proceeding
6. **AI File Manager:** Sends file list to Mistral AI for categorization suggestions
7. **Structured Output Parser:** Converts AI response to clean JSON
8. **Get Suggestions to List:** Splits AI suggestions into individual actions
9. **Move Files into Folders:** Creates folders as needed, moves files, handles duplicate renaming

Example: `invoice.pdf` -> moved to `Financial/Invoices/2025/2025-07-31_Invoice_XYZ-Company.pdf`

Template available: https://drive.google.com/file/d/1iWYUKLRxE5QA6SI-8Xw8FzLHPQjx5Rtj

**Document Processing and Data Extraction**
- OCR (Optical Character Recognition) reads text from scanned documents and images
- AI understands context and extracts specific fields (invoice number, date, vendor, amounts, line items)
- Output: Clean JSON data ready for accounting software

**PDF Generation and Manipulation**
- HTML-to-PDF conversion via Gotenberg for professional branded documents
- Dynamic data population for invoices, contracts, reports, certificates
- Merge, split, watermark, and password-protect PDFs

**Backup Systems**
- Automatically export n8n workflows as JSON to GitHub (version control)
- Schedule regular database dumps for self-hosted instances
- Follow the 3-2-1 Rule: 3 copies, 2 media types, 1 offsite copy

**Project: Automated Invoice Processing System**
Six-department architecture:
1. **Intake:** Monitors inbox for incoming vendor invoices
2. **Reading:** OCR + AI extract all relevant details from invoice PDFs
3. **Validation:** Verifies accuracy (e.g., line items total correctly)
4. **Filing:** Auto-renames and organizes into structured folder system
5. **Accounting:** Sends clean data to QuickBooks/Xero
6. **Oversight:** Routes high-value/unusual invoices for manual approval

### Task and Project Management Automation (8.2)

**Automatic Task Creation from Multiple Sources:**
- **Email-to-Task:** AI monitors inbox for action keywords, extracts details, creates tasks
- **Form-to-Task:** Webhook converts form submissions (bug reports, requests) into structured tasks
- **Chat-to-Task:** Monitors Slack/Teams for actionable messages, converts to trackable tasks

**Progress Tracking and Reporting:**
- Instant status updates when tasks move stages
- Automated weekly reports with charts (Google Sheets/Notion -> formatted email)
- Bottleneck detection: auto-identify stuck tasks and alert project managers

**Calendar and Meeting Management:**
- AI-powered natural language scheduling ("Schedule a call with Sarah next Tuesday")
- Meeting-to-task conversion: Transcription service (Fireflies.ai) -> AI extracts action items -> Creates structured tasks

## Key n8n Workflow Concepts

- Local File Trigger monitors filesystem for new files
- Mistral AI (and other LLMs) can classify and organize files intelligently
- Structured Output Parser converts AI text responses to clean JSON for downstream processing
- OCR + AI enables extraction of structured data from unstructured documents
- HTML-to-PDF via Gotenberg for dynamic document generation
- Webhook triggers convert form submissions to tasks instantly
- Sub-workflows separate concerns (intake, processing, filing, notification)

## Practical Takeaways for Scientists

- **Lab file organization:** The Mistral AI file organizer pattern is directly applicable to organizing experiment data, manuscripts, figures, and supplementary materials that accumulate in Downloads or shared drives
- **Automated data extraction from PDFs:** OCR + AI extraction is valuable for digitizing legacy lab notebooks, extracting data tables from published papers, or processing instrument-generated PDF reports
- **Invoice/expense automation for grants:** Automate tracking of grant-related expenses by extracting amounts from receipts and invoices, logging to spreadsheets, and flagging items that need PI approval
- **Meeting minutes to action items:** After lab meetings or committee sessions, use transcription + AI to automatically extract and assign action items to team members
- **Backup your workflows:** The automated workflow backup to GitHub pattern is essential -- treat your n8n workflows as code and version-control them
- **The 3-2-1 backup rule applies to research data too:** 3 copies, 2 media types, 1 offsite

## Notable References

- Mistral AI for file classification
- Gotenberg for HTML-to-PDF conversion
- Fireflies.ai for meeting transcription
- Template: https://drive.google.com/file/d/1iWYUKLRxE5QA6SI-8Xw8FzLHPQjx5Rtj
