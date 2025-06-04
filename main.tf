terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=4.1.0"
    }
  }
}
provider "azurerm" {
  features {}
  resource_provider_registration = "none"
}

terraform {
  backend "azurerm" {
    resource_group_name  = "rg-PiotrK"
    storage_account_name = "PiotrK"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}

resource "azurerm_service_plan" "example" {
  name                = "example-app-service-plan"
  location            = "westeurope"
  resource_group_name = "rg-PiotrK"
  os_type             = "Linux"
  sku_name            = "P0v3"
}


resource "azurerm_linux_web_app" "example" {
  name                = "example-webapp-123123i95u8fhwfdsewdwsa"
  location            = "westeurope"
  resource_group_name = "example-resources"
  service_plan_id     = azurerm_service_plan.example.id
  site_config {}
}
