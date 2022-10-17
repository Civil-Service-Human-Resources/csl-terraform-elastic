resource "ec_deployment" "csl_course_db_integration" {
  # Optional name.
  name = "elastic-integration-POC"

  # Mandatory fields
  region                 = "azure-uksouth"
  version                = "8.4.2"
  deployment_template_id = "azure-storage-optimized"

  elasticsearch {
    ref_id = "es-ref-id"
    config {
      user_settings_yaml = file("../../configuration/es-settings.yml")
    }

    topology {
      id                        = "hot_content"
      size                      = "2g"
      size_resource             = "memory"
      zone_count                = 1
    }
  }

  observability {
    deployment_id = ""
  }

  kibana {
    elasticsearch_cluster_ref_id = "es-ref-id"
    ref_id = "kibana-ref-id"
    topology {
      size = "1g"
      size_resource = "memory"
      zone_count = 1
    }
  }
}
