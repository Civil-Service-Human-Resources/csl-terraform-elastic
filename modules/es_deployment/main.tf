## Course DB
resource "ec_deployment" "csl_course_db" {
  # Optional name
  name = "csl-elastic-${var.env}"

  # Mandatory fields
  region                 = "azure-uksouth"
  version                = var.es_version
  deployment_template_id = "azure-storage-optimized"

  elasticsearch {
    ref_id = "es-ref-id"
    config {
      user_settings_yaml = file("../../configuration/es-settings.yml")
    }

    dynamic "topology" {
      for_each = var.es_topologies
      content {
        id                        = topology.value["type"]
        size                      = topology.value["size_in_gb"]
        size_resource             = "memory"
        zone_count                = topology.value["zones"]
      }
    }
  }

  observability {
    deployment_id = var.monitoring_deployment_id
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