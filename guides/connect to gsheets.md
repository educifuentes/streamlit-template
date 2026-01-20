# Connect Streamlit to Google Sheets

## 1. Google Cloud Setup
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Enable the **Google Sheets API**:
   - Go to **APIs & Services** > **Library**.
   - Search for "Google Sheets API" and click **Enable**.
4. Create Credentials:
   - Go to **APIs & Services** > **Credentials**.
   - Click **Create Credentials** > **Service Account**.
   - Fill in the details (name, description) and click **Create and Continue**.
   - (Optional) Grant "Editor" role if needed, or skip.
   - Click **Done**.
5. Generate Key:
   - Click on the newly created Service Account (email address).
   - Go to the **Keys** tab.
   - Click **Add Key** > **Create new key** > **JSON**.
   - The JSON key file will download automatically.

## 2. Share the Google Sheet
1. Create a new Google Sheet (e.g., "stocks-data").
2. Open the JSON key file you downloaded and copy the `client_email`.
3. In your Google Sheet, click **Share**.
4. Paste the `client_email` and ensure they have **Viewer** or **Editor** access.
5. Click **Send**.

## 3. Configure Secrets
Add your service account details to `.streamlit/secrets.toml`.

```toml
# .streamlit/secrets.toml

[connections.gsheets]
spreadsheet = "https://docs.google.com/spreadsheets/d/YOUR_SPREADSHEET_ID/edit"

# Content from your downloaded JSON key file
type = "service_account"
project_id = "xxx"
private_key_id = "xxx"
private_key = "xxx"
client_email = "xxx"
client_id = "xxx"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "xxx"
```

## 4. Usage in Streamlit

Ensure you have the connection library installed:
```bash
pip install streamlit-gsheets
```

Usage in your app:

```python
import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object
conn = st.connection("gsheets", type=GSheetsConnection)

# Read data
df = conn.read(
    worksheet="Sheet1",
    ttl="10m"
)

st.dataframe(df)
```

## References
- [Streamlit Docs: Connect to private Google Sheet](https://docs.streamlit.io/develop/tutorials/databases/private-gsheet)


