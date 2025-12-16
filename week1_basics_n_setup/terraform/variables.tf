variable "credentials" {
  description = "Path to GCP credentials JSON file"
  default = "./keys/my-creds.json"
}

variable "project" {
  description = "GCP Project ID"
  default = "terraform-demo-479204" 
}

variable "region" {
  description = "GCP Region"
  default = "us-central1"
}

variable "bq_dataset_name" {
  description = "My Bigquery Dataset Name"
  default = "my_dataset"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default = "STANDARD"
}

variable "location" {
  description = "Project Location"
  default = "EU"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default = "terraform-demo-479204-terraform-bucket"
}