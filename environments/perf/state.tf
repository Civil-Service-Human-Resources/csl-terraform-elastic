terraform {
  required_version = "~> 0.13.0"
  backend "azurerm" {
    resource_group_name = "lpgterraform"
    storage_account_name = "lpgterraformsecure"
    container_name = "tfstatesecure"
    key = "perf.elastic"
  }

  required_providers {
    ec = {
      source = "elastic/ec"
      version = "0.5.0"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.0.0"
    }
  }
}

provider "azurerm" {
  features {}
}
