variable "credentials" {
  description = "Path to GCP credentials JSON file"
  default = "/path/to/credentials.json"
}

variable "project" {
  description = "GCP Project ID"
  default = "my-project-id" 
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
  default = "my-project-id-terraform-bucket"
}