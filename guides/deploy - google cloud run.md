

guide



billing setup

1. Identify the Cloud Billing account linked to a project, guide in [Verify the billing status of your projects  |  Cloud Billing  |  Google Cloud Documentation](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project)



manage in [My Billing Account 1 – Overview – Billing – Google Cloud console](https://console.cloud.google.com/billing/014C05-76D442-66E69C)


instal google cli or use cloud shell in menu of project


Replace PROJECT_ID with your Google Cloud project ID and SERVICE_ACCOUNT_EMAIL_ADDRESS with the email address of the Cloud Build service account. If you're using the Compute Engine default service account as the Cloud Build service account, then use the following format for the service account email address:


gcloud projects add-iam-policy-binding analytics-dashboard-478018 \
    --member=serviceAccount:streamlit-PROJECT_NUMBER-compute@developer.gserviceaccount.com \
    --role=roles/run.builder



PROJECT_NUMBER-compute@developer.gserviceaccount.com

608973363066--compute@developer.gserviceaccount.com





gcloud projects add-iam-policy-binding analytics-dashboard-478018 \
    --member=serviceAccount:streamlit-edu-sample@analytics-dashboard-478018.iam.gserviceaccount.com \
    --role=roles/run.builder