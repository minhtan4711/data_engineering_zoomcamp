variable "project" {
  type        = string
  description = "GCP project ID"
}

variable "region" {
  type        = string
  description = "GCP region"
}

variable "zone" {
  type        = string
  description = "GCP zone"
}

variable "service_account_email" {
  type        = string
  description = "Service account email to impersonate"
}

variable "gcs_bucket_name" {
  type        = string
  description = "Globally unique bucket name"
}
