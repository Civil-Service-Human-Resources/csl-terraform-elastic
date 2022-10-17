terraform {
  required_version = "~> 0.13.0"

  required_providers {
    ec = {
      source = "elastic/ec"
      version = "0.4.1"
    }
  }
}
