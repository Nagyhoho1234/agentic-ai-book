# Chapter 3: Your First Real Automation

## Comprehensive Summary

Chapter 3 is a hands-on project chapter where you build a **Daily Weather Alert System** -- a practical automation that checks the weather every morning and sends a personalized notification. This project teaches three fundamental building blocks: Triggers, Actions, and Data Handling.

### Project: Daily Weather Alert System

**Step-by-step build process:**

1. **Create Workflow:** In the n8n dashboard, create and name a new workflow (e.g., "Daily Weather Alert")
2. **Schedule Trigger:** Add a Schedule Trigger node configured to run daily at your preferred time (e.g., 7:00 AM). Ensure the n8n instance timezone matches your local timezone.
3. **Get API Key:** Obtain a free API key from openweathermap.org (note: activation may take 1-2 hours)
4. **Add OpenWeatherMap Node:** Configure with your API key credential and city details to get current weather
5. **Format Weather Message:** Add a Set Node after OpenWeatherMap. Use expressions like `{{$('OpenWeatherMap').item.json.main.temp}}` to pull temperature, conditions, etc. into a formatted message
6. **Add Logic (Optional):** Insert an IF Node for conditional behavior (e.g., only alert if rain is expected)
7. **Send Notification:** Connect a Gmail, Slack, or Telegram node for delivery
8. **Connect and Test:** Link all nodes in sequence: Schedule Trigger -> OpenWeatherMap -> Set -> (Optional Logic) -> Notification. Click "Execute Workflow" to test.
9. **Activate:** Save and toggle to "Active" for automatic daily execution

### Testing and Debugging

Common issues and fixes:
- **API key not working:** Verify the key in Credentials, check the service status, ensure proper permissions/scopes
- **No notification arrives:** Check Output Data of the node preceding the notification node; check spam folders
- **Data mapping errors:** Referencing nonexistent fields (e.g., `city.name` vs. `city.city_name`). Use "Debug in Editor" to trace data and the Output panel to confirm expression matches

### Personalization Ideas

- Modify Schedule Trigger for weekdays only or alternate weekend times
- Use IF node for clothing suggestions based on temperature thresholds
- Use Switch node to assign weather emojis based on conditions
- Route severe weather alerts to SMS (via Twilio) while regular forecasts go to email only

## Key n8n Workflow Concepts

- **Schedule Trigger:** The digital alarm clock that starts workflows at predefined intervals
- **OpenWeatherMap Node:** Pre-built integration for weather data; requires API key credential
- **Set Node (Data Sculptor):** Creates new data fields and formats output using expressions wrapped in `{{ }}`
- **IF Node:** Binary decision-maker for conditional workflow paths
- **Expression syntax:** `{{$('NodeName').item.json.field.subfield}}` to reference data from specific nodes
- **Debug in Editor:** Loads failed execution data back onto the canvas for precise troubleshooting
- **Executions Tab:** Complete log of all workflow runs showing success/failure status

## Practical Takeaways for Scientists

- **The pattern is universal:** Schedule Trigger -> API call -> Data transformation -> Notification. This same pattern works for monitoring any data source -- instrument status, server health, data availability, or publication alerts.
- **API integration is a core skill:** Scientists who work with REST APIs (weather, satellite data, genomics) can apply this exact workflow pattern to automate data retrieval and alerting.
- **Conditional logic for thresholds:** The IF node pattern (e.g., alert only if temperature < 10) directly applies to scientific monitoring -- alert if sensor reading exceeds threshold, if disk space drops below limit, etc.
- **Expressions are the secret sauce:** Learning `{{ }}` expression syntax is the single most transferable skill across all n8n workflows.
- **Iterative testing:** The "Execute Workflow" button and node-by-node output inspection is the workflow equivalent of step-by-step debugging in code.

## Notable References

- OpenWeatherMap API: https://openweathermap.org
- Free API key required (may take 1-2 hours to activate)
