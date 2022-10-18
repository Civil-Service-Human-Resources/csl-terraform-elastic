### Course DB
module "es_course_db" {
  source = "../../modules/es_deployment"
  env = "integration"
  monitoring_deployment_id = ec_deployment.csl_test_monitoring.id
  es_topologies = [
    {
      type = "hot_content"
      size_in_gb = "2g"
      zones = 1
    }
  ]
}

# Logging and monitoring - this instance covers all 3 test regions
resource "ec_deployment" "csl_test_monitoring" {
  # Optional name.
  name = "elastic-test-monitoring"

  # Mandatory fields
  region                 = "azure-uksouth"
  version                = "8.4.3"
  deployment_template_id = "azure-storage-optimized"

  elasticsearch {
    ref_id = "es-ref-id"

    topology {
      id                        = "hot_content"
      size                      = "2g"
      size_resource             = "memory"
      zone_count                = 1
    }
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