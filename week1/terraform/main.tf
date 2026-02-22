# connect to gcp using adc
provider "google" {
  project = var.project
  region  = var.region
  zone    = var.zone
}

# this data source gets a temporary token for service account
data "google_service_account_access_token" "default" {
  provider               = google
  target_service_account = var.service_account_email
  scopes                 = ["https://www.googleapis.com/auth/cloud-platform"]
  lifetime               = "3600s"
}

# this second provider block uses that temporary token and does the real work
provider "google" {
  alias        = "impersonated"
  access_token = data.google_service_account_access_token.default.access_token
  project      = var.project
  region       = var.region
  zone         = var.zone
}

resource "google_storage_bucket" "demo" {
  provider = google.impersonated
  name     = var.gcs_bucket_name
  location = var.region
}
