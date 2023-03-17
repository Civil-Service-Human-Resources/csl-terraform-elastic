# Fetch the logging/monitoring stack
data "ec_deployments" "monitoring_deploy" {
  name_prefix = "elastic-test-monitoring"
  size = 1
}

### Course DB
module "es_course_db" {
  source = "../../modules/es_deployment"
  env = "staging"
  monitoring_deployment_id = data.ec_deployments.monitoring_deploy.deployments[0].deployment_id
  es_topologies = [
    {
      type = "hot_content"
      size_in_gb = "2g"
      zones = 1
    }
  ]
}