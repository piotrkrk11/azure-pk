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
  resource_provider_registrations = "none"
}

terraform {
  backend "azurerm" {
    resource_group_name  = "rg-PiotrK"
    storage_account_name = "stpiotrk"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}

resource "azurerm_service_plan" "example" {
  name                = "piotr-app-service-plan11"
  location            = "westeurope"
  resource_group_name = "rg-PiotrK"
  os_type             = "Linux"
  sku_name            = "P0v3"
}


resource "azurerm_linux_web_app" "example" {
  name                = "piotr-webapp-t2s-123"
  location            = "westeurope"
  resource_group_name = "rg-PiotrK"
  service_plan_id     = azurerm_service_plan.example.id
  site_config {}
}
