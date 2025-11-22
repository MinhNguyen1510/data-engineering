terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "7.10.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)  
  project = var.project
  region  = var.region
}

resource "google_storage_bucket" "auto-expire" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "dataset" {
    dataset_id = var.bq_dataset_name
    friendly_name = "test dataset"
    description = "This is a test description"
    location   = var.location
    default_table_expiration_ms = 3600000
    labels = {
      env = "dev"
    }
}